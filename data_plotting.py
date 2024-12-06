import matplotlib.pyplot as plt


def create_and_save_plot(data, ticker, period, filename=None):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 18), sharex=True)

    # График цены закрытия и скользящего среднего
    ax1.plot(data.index, data['Close'], label='Цена закрытия')
    ax1.plot(data.index, data['MA'], label='Скользящее среднее')
    ax1.set_title(f'Цена акции {ticker} за период {period}')
    ax1.set_ylabel('Цена')
    ax1.legend()

    # График RSI
    ax2.plot(data.index, data['RSI'], label='RSI', color='purple')
    ax2.axhline(y=70, color='red', linestyle='--')
    ax2.axhline(y=30, color='green', linestyle='--')
    ax2.set_title('Relative Strength Index RSI(индекс относительной силы)')
    ax2.set_ylabel('RSI')
    ax2.set_ylim(0, 100)
    ax2.legend()

    # График MACD
    ax3.plot(data.index, data['MACD'], label='MACD', color='blue')
    ax3.plot(data.index, data['Signal_Line'], label='Signal Line', color='orange')
    ax3.bar(data.index, data['MACD_Histogram'], label='MACD Histogram', color='gray', alpha=0.3)
    ax3.set_title('Moving Average Convergence Divergence MACD (схождение-расхождение скользящих средних)')
    ax3.set_xlabel('Дата')
    ax3.set_ylabel('MACD')
    ax3.legend()

    plt.tight_layout()

    if filename:
        plt.savefig(filename)
    else:
        plt.savefig(f'{ticker}_{period}.png')

    plt.show()