import matplotlib.pyplot as plt


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Цена закрытия')
    plt.plot(data.index, data['MA'], label='Скользящее среднее')
    plt.title(f'Цена акции {ticker} за период {period}')
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.legend()

    if filename:
        plt.savefig(filename)
    else:
        plt.savefig(f'{ticker}_{period}.png')

    plt.show()
