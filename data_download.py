import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_stock_data(ticker, start_date=None, end_date=None, period=None):
    """
    Загружает данные о ценах акций для заданного тикера.

    Args:
        ticker (str): Тикер акции.
        start_date (str, optional): Дата начала в формате 'YYYY-MM-DD'.
        end_date (str, optional): Дата окончания в формате 'YYYY-MM-DD'.
        period (str, optional): Период для загрузки данных (например, '1mo', '1y').

    Returns:
        pandas.DataFrame: DataFrame с историческими данными акции.

    Raises:
        ValueError: Если не указаны ни период, ни даты начала и окончания.
    """
    stock = yf.Ticker(ticker)

    if start_date and end_date:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        data = stock.history(start=start, end=end)
    elif period:
        data = stock.history(period=period)
    else:
        raise ValueError("Необходимо указать либо период, либо даты начала и окончания")

    return data

def add_moving_average(data, window_size=20):
    """
    Добавляет скользящее среднее к DataFrame с данными акций.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций.
        window_size (int, optional): Размер окна для расчета скользящего среднего. По умолчанию 20.

    Returns:
        pandas.DataFrame: DataFrame с добавленным столбцом 'MA' (скользящее среднее).
    """
    data['MA'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    """
    Вычисляет и выводит среднюю цену закрытия акций.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций.
    """
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия акций: {average_price:.2f}")

def notify_if_strong_fluctuations(data, threshold):
    """
    Анализирует колебания цены акций и уведомляет о сильных изменениях.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций.
        threshold (float): Пороговое значение колебаний в процентах.
    """
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

def export_data_to_csv(data, filename):
    """
    Экспортирует данные об акциях в CSV файл.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций.
        filename (str): Имя файла для сохранения данных.
    """
    try:
        data.to_csv(filename, index=True)
        print(f"Данные успешно экспортированы в {filename}")
    except Exception as e:
        print(f"Произошла ошибка при экспорте данных: {e}")

def add_rsi(data, window=14):
    """
    Добавляет индекс относительной силы (RSI) к DataFrame с данными акций.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций.
        window (int, optional): Размер окна для расчета RSI. По умолчанию 14.

    Returns:
        pandas.DataFrame: DataFrame с добавленным столбцом 'RSI'.
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

def add_macd(data, short_window=12, long_window=26, signal_window=9):
    """
    Добавляет индикатор MACD к DataFrame с данными акций.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций.
        short_window (int, optional): Короткое окно EMA. По умолчанию 12.
        long_window (int, optional): Длинное окно EMA. По умолчанию 26.
        signal_window (int, optional): Окно сигнальной линии. По умолчанию 9.

    Returns:
        pandas.DataFrame: DataFrame с добавленными столбцами 'MACD', 'Signal_Line' и 'MACD_Histogram'.
    """
    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = short_ema - long_ema
    data['Signal_Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    data['MACD_Histogram'] = data['MACD'] - data['Signal_Line']
    return data

def add_standard_deviation(data, window=20):
    """
    Добавляет стандартное отклонение к DataFrame с данными акций.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций.
        window (int, optional): Размер окна для расчета стандартного отклонения. По умолчанию 20.

    Returns:
        pandas.DataFrame: DataFrame с добавленным столбцом 'StdDev'.
    """
    data['StdDev'] = data['Close'].rolling(window=window).std()
    return data
