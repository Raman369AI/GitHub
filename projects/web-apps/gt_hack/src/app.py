import os
import torch
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
OLLAMA_API_BASE = os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")
OLLAMA_API_KEY = os.environ.get("OLLAMA_API_KEY", "")

if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY environment variable is required")
    st.stop()

torch.classes.__path__ = []
torch.set_num_threads(1)

from smolagents import CodeAgent, LiteLLMModel, tool

model = LiteLLMModel(
    model_id="ollama_chat/deepseek-r1:8b",
    api_base=OLLAMA_API_BASE,
    api_key=OLLAMA_API_KEY,
    num_ctx=8192
)

model_1 = LiteLLMModel(
    model_id="ollama_chat/qwen2.5-coder:latest",
    api_base=OLLAMA_API_BASE,
    api_key=OLLAMA_API_KEY,
    num_ctx=16000
)

@tool
def mathematical_agent_tool() -> str:
    '''This is a tool which forecasts 6 month forecasts, 
     it returns a string variable called sentence and it is equal to all the execution logs
    Args:
        '''
    import pandas as pd
    import numpy as np
    from pmdarima import auto_arima

    data_file = os.environ.get("PRICE_DATA_FILE", "data/iphone_price_trends_updated.csv")
    
    if not os.path.exists(data_file):
        return "Error: Price data file not found. Please ensure the data file is available."
    
    prices = pd.read_csv(data_file)
    prices = prices.dropna(how='all')
    prices['Date'] = pd.to_datetime(prices['Date'], format='%Y-%m')
    df = prices[0:46]
    df.set_index('Date', inplace=True)

    y = df['New']
    X = df[['CPIAUCSL', 'Unemployment_Rate', 'Interest Rates','CPI']]

    # Fit the AutoARIMAX model
    model = auto_arima(
        y,
        exogenous=X,
        start_p=1, max_p=1,          # Constrain AR (p) to 1
        start_q=4, max_q=4,          # Constrain MA (q) to 4
        d=1,   
        seasonal=False,           # Set to True if seasonality is suspected
        trace=True,               # Display progress of parameter search
        suppress_warnings=True,
        stepwise=True             # Perform stepwise parameter selection
    )
    model.fit_with_exog_
    # Print the selected ARIMAX order
    print(f"Best ARIMAX order: {model.order}")
    print(f"Best Seasonal Order: {model.seasonal_order}")

    # Forecast next 6 months (provide future values for exogenous variables)
    future_dates = pd.date_range(start='2024-07-01', periods=6, freq='M')
    future_exog = pd.DataFrame({
        'CPIAUCSL': prices['CPIAUCSL'][46:].values,
        'Unemployment_Rate': prices['Unemployment_Rate'][46:].values,
        'Interest Rates': prices['Interest Rates'][46:].values,
        'CPI': prices['CPI'][46:].values,
    }, index=future_dates)
    print(future_exog)

    # Make predictions
    forecast = model.predict(n_periods=6, exogenous=future_exog)

    # Combine forecast with future dates
    forecast_df = pd.DataFrame({'Date': future_dates, 'Forecasted New Price': forecast})
    forecast_df.set_index('Date', inplace=True)

    # Display forecasted prices
    future_exog = pd.DataFrame({
        'CPIAUCSL': prices['CPIAUCSL'][46:],
        'Unemployment_Rate': prices['Unemployment_Rate'][46:],
        'Interest Rates': prices['Interest Rates'][46:],
        'CPI': prices['CPI'][46:],
    }, index=future_dates)
    forecast = model.predict(n_periods=6, exogenous=future_exog)
    sentence = ', '.join([f"{index.strftime('%Y-%m-%d')} the price is {round(value,2)}" for index, value in forecast.items()])
    return sentence
mathematical_agent = CodeAgent(tools=[mathematical_agent_tool], model=model_1,additional_authorized_imports=["*"],  add_base_tools=False, max_steps = 5, verbosity_level = 5, name = 'mathematical_agent', description = "access ###'iphone_price_trends_updated.csv' in the current working directory and give the name of the csv as input to mathematical_agent_tool, dont modify the final sentence variable the out should be the sentence as it is" )
@tool
def market_preds(sentence: str) -> str:
    """
    Returns the interpretation of the forecasts from the purview of the real word events
    This is about a product called Apple Iphone 12 128 GB, you will take the the forecast of the price in dollars 
    and give the macroeconomic or product related or Geopolitical or other events that influenced the increase or 
    decrease, refer internet for the events

    Args:
        sentence: the forecasts for 6 months
    """
    description = """
    This is about a product called Apple Iphone 12 128 GB, you will take the the forecast of the price in dollars 
    and give the macroeconomic or product related or Geopolitical or other events that influenced the increase or decrease, 
    refer internet for the events"""
    import os
    import google.generativeai as genai

    genai.configure(api_key=GEMINI_API_KEY)
    generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 4096,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-pro-exp-02-05",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[]
    )
    events = chat_session.send_message(f'''Give me all events from February 2020 to February 2025 in month and 
                                       year format that affect apple's supply chain or events that can affect 
                                       the price of a iphone, including supply chain , quality issues, competitor 
                                       launch, or new product launch, geopolitics, tariffs, China, taiwan, 
                                       antitrust and quality issues''')
    
    response = chat_session.send_message(f'''{sentence} is the forecast of iphone 12 128GB for 6 months and {events.text} are the events 
                                         that can affect the price of an iphone, evaluate the forecast and events 
                                         and associate each forecast with the corresponding event and give your entire
                                          thought process and observations''' )
    return response.text

market_agent = CodeAgent(tools=[market_preds], model=model_1,  add_base_tools=False, max_steps = 5, verbosity_level = 5, name = "market_agent", additional_authorized_imports=["*"],description = 'This agent helps in doing market research for the product described and returns the interpreted message')
from smolagents import ToolCallingAgent,CodeAgent
from smolagents.default_tools import FinalAnswerTool,DuckDuckGoSearchTool, VisitWebpageTool

web_agent = CodeAgent(tools=[DuckDuckGoSearchTool(),VisitWebpageTool()], model=model_1,  add_base_tools=True, max_steps = 5, verbosity_level = 5 , additional_authorized_imports=["*"], name = "web_agent", description = "Write code to go to duckduckgo and for iphone shipments and redo the same iphone revenue share, sumamrize the search results be specific with numbers and years , try to get years 2020 to 2025 and print the summary")

#Recommendation Agent
@tool
def recommend_tool(sentence: str, web_search: str, market:list) -> str:
    """
    Returns the pricing optimization advice

    Args:
        sentence: the forecasts for 6 months
        web_search: The quantities and revenue associated with the iphone sales
        market: The events that affect the iphone price and their mapping with the forecast
    """
    description = """
    This is about a product called Apple Iphone 12 128 GB, you will take the the forecast of the price in dollars and 
    give the macroeconomic or product related or Geopolitical or other events that influenced the increase or decrease, 
    refer internet for the events"""
    import os
    import google.generativeai as genai

    genai.configure(api_key=GEMINI_API_KEY)
    generation_config = {
        "temperature": 0.1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 4096,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-pro-exp-02-05",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[]
    )
    total = sentence + web_search +' '.join(market)
    response = chat_session.send_message(f'''{total} is the output of all the three agents, the forecasts for the next 6 months , 
                                         the events that might have impacted the iphone price and historical revenue and quantity numbers,
                                          now based on all these try price elasticity and other price optimisation and dynamic pricing 
                                         theories and give a condensed recommendation of the pricing strategy along with the future 
                                         expectations of the price ''')
    return response.text
recommend_agent = CodeAgent(tools=[recommend_tool], model=model_1,  add_base_tools=False, max_steps = 5, verbosity_level = 5, name = "recommend_agent", additional_authorized_imports=["*"],description = 'This agent helps in consolidating the outputs of the other three and gives the pricing strategy recommendations')
import torch
import streamlit as st
torch.set_num_threads(1)
# Page setup with basic styling
st.set_page_config(layout="wide")

# Simple CSS for font
st.markdown("""
    <style>
    * {
        font-family: 'Arial', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Analysis Parameters")
    st.info("iPhone pricing and market analysis tool")

# Main input
prompt = st.text_input("Enter your prompt...")

if st.button('Start Analysis'):
    if prompt:
        try:
            # Mathematical Analysis
            st.subheader("Mathematical Analysis")
            with st.spinner('Running mathematical analysis...'):
                sentence = mathematical_agent.run(prompt)
                st.text(sentence)

            # Market Analysis
            st.subheader("Market Analysis")
            with st.spinner('Running market analysis...'):
                market = market_agent.run(f'''{sentence} is the input to the market_preds and the forecast of iphone 12 128GB for 6 months 
                                          and the events that can affect the price of an iphone, evaluate the forecast and events and 
                                          associate each forecast with the corresponding event and give an elaborate association of events 
                                          and price forecast''' )
                st.text(market)

            # Web Search
            st.subheader("Web Search Results")
            with st.spinner('Searching web...'):
                web_search = web_agent.run(f"""search for quanitity of iphone shipments and
                                            redo the same for iphone revenue share, sumamrize the search results be specific with numbers and years ,
                                            try to get years 2020 to 2025 and print as a complete sentence by sumamrizing the search results of each year
                                            with any additional information with the quantities and revenue for each year""")
                st.text(web_search)

            # Recommendations
            st.subheader("Recommendations")
            with st.spinner('Generating recommendations...'):
                recommendation = recommend_agent.run('''Given are the output of all the three agents, the forecasts for the next 6 months , 
                                                     the events that might have impacted the iphone price and historical revenue and quantity numbers, 
                                                     now based on all these try price elasticity and other price optimisation and dynamic pricing theories 
                                                     and give a condensed recommendation of the pricing strategy along with the future expectations of 
                                                     the average price for  all iphone models in common and also the risks associated, geopolitical, 
                                                     social, economic, macro economic, monetary summarize in one paragraph''')
                st.text(recommendation)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a prompt to begin analysis")






