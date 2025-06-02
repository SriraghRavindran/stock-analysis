import requests
import yfinance as yf

def getStockData(stock_name, start_date, end_date):
    data = yf.download(stock_name+'.NS',start_date,end_date)
    return data
