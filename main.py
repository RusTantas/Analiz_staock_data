from data_download import fetch_stock_data, add_moving_average, calculate_and_display_average_price
from data_plotting import create_and_save_plot


def main():
    ticker = input("Введите тикер акции (например, AAPL): ")
    period = input("Введите период (например, 1mo, 1y, max): ")

    try:
        data = fetch_stock_data(ticker, period)
        data = add_moving_average(data)
        create_and_save_plot(data, ticker, period)
        data = fetch_stock_data(ticker, period)
        calculate_and_display_average_price(data)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()