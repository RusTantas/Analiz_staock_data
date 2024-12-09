from data_download import *
from data_plotting import create_and_save_plot
from datetime import datetime


def process_data(data, ticker, start_date, end_date):
    data = add_moving_average(data)
    data = add_rsi(data)
    data = add_macd(data)
    calculate_and_display_average_price(data)

    threshold = float(input("Введите пороговое значение для сильных колебаний (в %): "))
    notify_if_strong_fluctuations(data, threshold)

    filename = f"{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    export_data_to_csv(data, filename)
    create_and_save_plot(data, ticker, start_date, end_date)


def main():
    ticker = input("Введите тикер акции (например, AAPL): ")
    date_choice = input("Выберите способ указания периода (1 - предустановленный период, 2 - конкретные даты): ")

    try:
        if date_choice == "1":
            period = input("Введите период (например, 1mo, 1y, max): ")
            data = fetch_stock_data(ticker, period=period)
            process_data(data, ticker, period, period)
        elif date_choice == "2":
            start_date = input("Введите дату начала в формате YYYY-MM-DD: ")
            end_date = input("Введите дату окончания в формате YYYY-MM-DD: ")
            data = fetch_stock_data(ticker, start_date=start_date, end_date=end_date)
            process_data(data, ticker, start_date, end_date)
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()