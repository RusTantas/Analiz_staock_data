import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def create_and_save_plot(data, ticker, start_date, end_date, filename=None):
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 20), sharex=True)

    # График цены закрытия и скользящего среднего
    ax1.plot(data.index, data['Close'], label='Цена закрытия')
    ax1.plot(data.index, data['MA'], label='Скользящее среднее')
    ax1.set_title(f'Анализ акции {ticker} с {start_date} по {end_date}')
    ax1.set_ylabel('Цена')
    ax1.legend()

    # График RSI
    ax2.plot(data.index, data['RSI'], label='RSI', color='purple')
    ax2.axhline(y=70, color='red', linestyle='--')
    ax2.axhline(y=30, color='green', linestyle='--')
    ax2.set_ylabel('RSI')
    ax2.set_ylim(0, 100)
    ax2.legend()

    # График MACD
    ax3.plot(data.index, data['MACD'], label='MACD', color='blue')
    ax3.plot(data.index, data['Signal_Line'], label='Сигнальная линия', color='orange')
    ax3.bar(data.index, data['MACD_Histogram'], label='Гистограмма MACD', color='gray', alpha=0.3)
    ax3.set_ylabel('MACD')
    ax3.legend()

    # График объема торгов
    ax4.bar(data.index, data['Volume'], label='Объем', color='lightblue')
    ax4.set_ylabel('Объем')
    ax4.set_xlabel('Дата')
    ax4.legend()

    # Настройка формата даты на оси X
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax4.xaxis.set_major_locator(mdates.AutoDateLocator())

    plt.tight_layout()

    if filename:
        plt.savefig(filename)
    else:
        plt.savefig(f'{ticker}_{start_date}_{end_date}.png')

    plt.show()