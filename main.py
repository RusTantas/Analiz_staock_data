from data_download import *
from data_plotting import create_and_save_plot


def main():
    ticker = input("Введите тикер акции (например, AAPL): ")
    period = input("Введите период (например, 1mo, 1y, max): ")

    try:
        data = fetch_stock_data(ticker, period)
        data = add_moving_average(data)
        data = add_rsi(data)
        data = add_macd(data)
        create_and_save_plot(data, ticker, period)
        data = fetch_stock_data(ticker, period)
        calculate_and_display_average_price(data)
        data = fetch_stock_data(ticker, period)
        notify_if_strong_fluctuations(data, 5)  # 5% - пример порогового значения задаеться пользователем
        export_data_to_csv(data, 'Выгрузка')
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
