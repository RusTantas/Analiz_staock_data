from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import matplotlib.pyplot as plt

def predict_stock_price(data, periods=30):
    """
    Прогнозирует цены акций на основе исторических данных, используя модель ARIMA.

    Args:
        data (pandas.DataFrame): DataFrame с историческими данными акций, содержащий столбец 'Close'.
        periods (int, optional): Количество периодов для прогнозирования. По умолчанию 30.

    Returns:
        pandas.Series: Серия с прогнозируемыми ценами акций.

    Raises:
        ValueError: Если входные данные некорректны или недостаточны для построения модели.
    """
    model = ARIMA(data['Close'], order=(1, 1, 1))
    results = model.fit()
    forecast = results.forecast(steps=periods)
    return forecast

def plot_prediction(data, forecast, ticker):
    """
    Создает график с историческими данными и прогнозом цен акций.

    Args:
        data (pandas.DataFrame): DataFrame с историческими данными акций.
        forecast (pandas.Series): Серия с прогнозируемыми ценами акций.
        ticker (str): Тикер акции для заголовка графика.

    Returns:
        None: Функция отображает график, но не возвращает значение.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Исторические данные')
    forecast_dates = pd.date_range(start=data.index[-1], periods=len(forecast) + 1)[1:]
    plt.plot(forecast_dates, forecast, label='Прогноз', color='red')
    plt.title(f'Прогноз цены акции {ticker}')
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.legend()

    plt.text(0.5, -0.1, "Внимание: Этот прогноз не является инвестиционной рекомендацией",
             ha='center', va='center', transform=plt.gca().transAxes, fontsize=10, color='red')

    plt.tight_layout()
    plt.show()

def run_prediction(data, ticker):
    """
    Выполняет прогнозирование цен акций и отображает результаты.

    Эта функция объединяет процессы прогнозирования и визуализации результатов.

    Args:
        data (pandas.DataFrame): DataFrame с историческими данными акций.
        ticker (str): Тикер акции.

    Returns:
        None: Функция отображает график, но не возвращает значение.
    """
    forecast = predict_stock_price(data)
    plot_prediction(data, forecast, ticker)
