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

