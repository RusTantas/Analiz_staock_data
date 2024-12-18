from data_download import *
from data_plotting import create_interactive_plot, calculate_and_display_average_price
from datetime import datetime
from stock_prediction import run_prediction


def process_data(data, ticker, start_date, end_date, style):
    data = add_moving_average(data)
    data = add_rsi(data)
    data = add_macd(data)
    data = add_standard_deviation(data)  # Добавляем новую функцию

    calculate_and_display_average_price(data)

    threshold = float(input("Введите пороговое значение для сильных колебаний (в %): "))
    notify_if_strong_fluctuations(data, threshold)

    filename = f"{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    export_data_to_csv(data, filename)
    create_interactive_plot(data, ticker, start_date, end_date)
    avg_price = calculate_and_display_average_price(data)


def main():
    ticker = input("Введите тикер акции (например, AAPL): ")
    date_choice = input("Выберите способ указания периода (1 - предустановленный период, 2 - конкретные даты): ")

    style_map = {
        "1": "default",
        "2": "ggplot",
        "3": "seaborn",
        "4": "dark_background"
    }
    print("Доступные стили графиков:")
    for key, value in style_map.items():
        print(f"{key}. {value}")
    style_choice = input("Выберите номер стиля (или нажмите Enter для стиля по умолчанию): ")
    style = style_map.get(style_choice, "default")

    try:
        if date_choice == "1":
            period = input("Введите период (например, 1mo, 1y, max): ")
            predict_choice = input("Хотите выполнить прогноз? (y/n): ")
            data = fetch_stock_data(ticker, period=period)
            process_data(data, ticker, period, period, style)
            if predict_choice.lower() == 'y':
                run_prediction(data, ticker)

        elif date_choice == "2":
            start_date = input("Введите дату начала в формате YYYY-MM-DD: ")
            end_date = input("Введите дату окончания в формате YYYY-MM-DD: ")
            data = fetch_stock_data(ticker, start_date=start_date, end_date=end_date)
            process_data(data, ticker, start_date, end_date, style)
            predict_choice = input("Хотите выполнить прогноз? (y/n): ")
            if predict_choice.lower() == 'y':
                run_prediction(data, ticker)

    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
