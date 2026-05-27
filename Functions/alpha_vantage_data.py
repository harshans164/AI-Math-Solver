from dotenv import load_dotenv
import os
import requests
from pprint import pprint

from google.genai import types

alpha_vantage_data_schema = types.FunctionDeclaration(
         name="alpha_vantage_data",
         description="This function uses the alpha vantage api to get live stock details of a company. This function can be used to get live news or analytics of a company. Useful for understanding the trend of a company.", # FIX: Added missing comma
         parameters=types.Schema(
              type=types.Type.OBJECT,
              properties={
                   "symbol": types.Schema(
                        type=types.Type.STRING,
                        description="Ticker symbol of the company in stock exchange, example: google: GOOG, apple : AAPL."
                   ),
                   "types": types.Schema(
                        type=types.Type.STRING,
                        description="Used to obtain news or analytics of a company. Setting parameters as 'news', gives news related to that company. Setting parameter as 'analytics', gives analytics of that company."                  
                   ),
                   "year": types.Schema(
                        type=types.Type.STRING,
                        description="Used only in analytics, to get the company's analytics in that particular year. In news this can be avoided. Ex : to get analytics for the year 2023, then use: '2023'"                   
                   ),
                   "quarter": types.Schema(
                        type=types.Type.STRING,
                        description="Used only in analytics, to get the company's analytics in that particular quarter. In news this can be avoided. Ex: to get analytics in 2nd quarter use : Q2, for 3rd quarter Q3, similarly for 1st and 4th quarter."                    
                   ) 
              },
              required=["symbol", "types"] 
         )
    )


def alpha_vantage_data(symbol, types, year = None, quarter = None):
    load_dotenv()
    VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
    key=""
    info=""
    if types=="news":
        url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers='+symbol+f'&apikey="{VANTAGE_API_KEY}"'
        key="feed"
        info+="News data from alpha vantage: \n"

    if types=="analytics":
        url = 'https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&symbol='+symbol+'&quarter='+year+ quarter + f'&apikey="{VANTAGE_API_KEY}"'
        key="transcript"
        info+="Analytics data from alpha vantage: \n"

    
    r = requests.get(url)
    data = r.json()
    for index, d in enumerate(data['transcript']):
            info+=str(index)+"." 
            info+=d['title']
            info+="\n"
            if types=="news":
                info+=d['summary']
            elif types=="analytics":
                 info+=d['content']
            info+="\n"

    pprint(info)





if __name__=="__main__":
    # alpha_vantage_data("GOOG","analytics","2025","Q4")
    alpha_vantage_data("GOOG","news")

    