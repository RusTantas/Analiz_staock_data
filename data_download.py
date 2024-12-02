import yfinance as yf
import pandas as pd

'''
Загрузка ДФ
'''
def fetch_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

'''
Формирование столбика МА цена на закрытии
'''
def add_moving_average(data, window_size=20):
    data['MA'] = data['Close'].rolling(window=window_size).mean()
    return data

'''

calculate_and_display_average_price
Цель:
Вычисляет и выводит среднюю цену закрытия акций за заданный период.
Реализация:
Функция будет принимать DataFrame и вычислять среднее значение колонки 'Close'. Результат будет выводиться в консоль.
'''
def calculate_and_display_average_price(data):
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия акций: {average_price:.2f}")


'''
notify_if_strong_fluctuations
Цель:
Анализирует данные и уведомляет  пользователя, если цена акций колебалась более чем на заданный процент за период.
Реализация:
Функция будет вычислять максимальное и минимальное значения цены закрытия и сравнивать разницу 
с заданным порогом. Если разница превышает порог, пользователь получает уведомление.
'''
def notify_if_strong_fluctuations(data, threshold):
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    fluctuation = (max_price - min_price) / min_price * 100

    if fluctuation > threshold:
        print(f"Внимание! Обнаружены сильные колебания цены.")
        print(f"Максимальная цена: {max_price:.2f}")
        print(f"Минимальная цена: {min_price:.2f}")
        print(f"Колебание: {fluctuation:.2f}%")
    else:
        print(f"Сильных колебаний цены не обнаружено. Максимальное колебание: {fluctuation:.2f}%")
