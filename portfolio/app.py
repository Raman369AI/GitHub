import asyncio
import json
import ssl
import upstox_client
import websockets
from google.protobuf.json_format import MessageToDict
from google.cloud import pubsub_v1
import MarketDataFeed_pb2 as pb
import json

import json

def filter_i1_data(json_string):
    """
    Filters a JSON string to select only the I1 interval data from the ohlc list.

    Args:
        json_string: A JSON string representing the Upstox market data.

    Returns:
        The first dictionary representing an I1 interval,
        or an empty list if no I1 data is found or if there's an error.
    """
    try:
        data = json.loads(json_string)
        ohlc_data = data.get("feeds", {}).get("NSE_INDEX|Nifty Bank", {}).get("ff", {}).get("indexFF", {}).get("marketOHLC", {}).get("ohlc", [])
        i1_data = [item for item in ohlc_data if item.get("interval") == "I1"]
        if i1_data:
            return i1_data[0]  # Return only the first dictionary
        else:
            return []  # Return an empty list if no I1 data is found
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def get_market_data_feed_authorize(api_version, configuration):
    """Get authorization for market data feed."""
    api_instance = upstox_client.WebsocketApi(
        upstox_client.ApiClient(configuration))
    api_response = api_instance.get_market_data_feed_authorize(api_version)
    return api_response


def decode_protobuf(buffer):
    """Decode protobuf message."""
    feed_response = pb.FeedResponse()
    feed_response.ParseFromString(buffer)
    return feed_response


async def fetch_market_data():
    """Fetch market data using WebSocket and print it."""

    # Create default SSL context
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Configure OAuth2 access token for authorization
    configuration = upstox_client.Configuration()

    api_version = '2.0'
    configuration.access_token = ''

    # Get market data feed authorization
    response = get_market_data_feed_authorize(
        api_version, configuration)

    # Connect to the WebSocket with SSL context
    async with websockets.connect(response.data.authorized_redirect_uri, ssl=ssl_context) as websocket:
        print('Connection established')

        await asyncio.sleep(1)  # Wait for 1 second

        # Data to be sent over the WebSocket
        data = {
            "guid": "someguid",
            "method": "sub",
            "data": {
                "mode": "full",
                "instrumentKeys": ["NSE_INDEX|Nifty Bank", "NSE_INDEX|Nifty 50"]
            }
        }

        # Convert data to binary and send over WebSocket
        binary_data = json.dumps(data).encode('utf-8')
        await websocket.send(binary_data)
        publisher = pubsub_v1.PublisherClient()
        subscriber = pubsub_v1.SubscriberClient()
        topic_path = publisher.topic_path('crafty-dynamics-451718-v8', 'my-topic')

        # Continuously receive and decode data from WebSocket
        while True:
            message = await websocket.recv()
            decoded_data = decode_protobuf(message)

            # Convert the decoded data to a dictionary
            data_dict = MessageToDict(decoded_data)

            # Print the dictionary representation
            data = json.dumps(data_dict).encode("utf-8")
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
            
            #future = publisher.publish(topic_path, data)

            if data:
    # Convert the filtered data to JSON string
                filtered_json_string = json.dumps(data).encode("utf-8")
                future = publisher.publish(topic_path, filtered_json_string)
                print(f"Published message ID: {future.result()}")
            else:
                print("No I1 data found in this message.")
          
asyncio.run(fetch_market_data())