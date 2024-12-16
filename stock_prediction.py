from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import matplotlib.pyplot as plt


def predict_stock_price(data, periods=30):
    model = ARIMA(data['Close'], order=(1, 1, 1))
    results = model.fit()
    forecast = results.forecast(steps=periods)
    return forecast


def plot_prediction(data, forecast, ticker):
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
    forecast = predict_stock_price(data)
    plot_prediction(data, forecast, ticker)
