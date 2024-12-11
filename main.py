from data_download import *
from data_plotting import create_and_save_plot
from datetime import datetime

def process_data(data, ticker, start_date, end_date, style):
    """
    Обрабатывает данные: добавляет индикаторы, рассчитывает средние значения,
    проверяет колебания и строит график.
    """
    try:
        # Добавляем технические индикаторы
        data = add_moving_average(data)
        data = add_rsi(data)
        data = add_macd(data)

        # Рассчитываем среднюю цену
        calculate_and_display_average_price(data)

        # Проверяем сильные колебания
        threshold = float(input("Введите пороговое значение для сильных колебаний (в %): "))
        notify_if_strong_fluctuations(data, threshold)

        # Экспортируем данные в CSV
        filename = f"{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        export_data_to_csv(data, filename)
        print(f"Данные успешно сохранены в файл: {filename}")

        # Создаем график
        create_and_save_plot(data, ticker, start_date, end_date, style=style)

    except Exception as e:
        print(f"Произошла ошибка при обработке данных: {e}")

def main():
    """
    Основная функция программы. Запрашивает у пользователя параметры анализа и запускает обработку данных.
    """
    ticker = input("Введите тикер акции (например, AAPL): ")

    # Выбор способа указания периода
    date_choice = input("Выберите способ указания периода (1 - предустановленный период, 2 - конкретные даты): ")

    # Выбор стиля графика
    print("Доступные стили графиков:")
    print("1. default")
    print("2. ggplot")
    print("3. seaborn")
    print("4. dark_background")
    style_choice = input("Выберите номер стиля (или нажмите Enter для стиля по умолчанию): ")

    style_map = {
        "1": "default",
        "2": "ggplot",
        "3": "seaborn",
        "4": "dark_background"
    }
    style = style_map.get(style_choice, "default")

    try:
        if date_choice == "1":
            # Пользователь выбирает предустановленный период
            period = input("Введите период (например, 1mo, 1y, max): ")
            data = fetch_stock_data(ticker, period=period)
            process_data(data, ticker, period, period, style)

        elif date_choice == "2":
            # Пользователь вводит конкретные даты
            start_date = input("Введите дату начала в формате YYYY-MM-DD: ")
            end_date = input("Введите дату окончания в формате YYYY-MM-DD: ")
            data = fetch_stock_data(ticker, start_date=start_date, end_date=end_date)
            process_data(data, ticker, start_date, end_date, style)

        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
if __name__ == "__main__":
    main()
