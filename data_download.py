import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

def add_moving_average(data, window_size=20):
    data['MA'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия акций: {average_price:.2f}")