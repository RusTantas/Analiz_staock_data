import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_interactive_plot(data, ticker, start_date, end_date):
    """
    Создает интерактивный график для анализа акций с использованием Plotly.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций, включая 'Close', 'MA', 'RSI', 'MACD', 'Signal_Line', 'MACD_Histogram' и 'Volume'.
        ticker (str): Тикер акции.
        start_date (str): Дата начала периода анализа.
        end_date (str): Дата окончания периода анализа.

    Returns:
        None: Функция отображает график, но не возвращает значение.

    The function creates a multi-panel interactive plot with the following components:
    1. Stock price and moving average
    2. RSI (Relative Strength Index)
    3. MACD (Moving Average Convergence Divergence)
    4. Trading volume
    """
    fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.05,
                        subplot_titles=('Цена акции', 'RSI', 'MACD', 'Объем торгов'))

    # График цены закрытия и скользящего среднего
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Цена закрытия'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['MA'], name='Скользящее среднее'), row=1, col=1)

    # График RSI
    fig.add_trace(go.Scatter(x=data.index, y=data['RSI'], name='RSI'), row=2, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)

    # График MACD
    fig.add_trace(go.Scatter(x=data.index, y=data['MACD'], name='MACD'), row=3, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['Signal_Line'], name='Сигнальная линия'), row=3, col=1)
    fig.add_trace(go.Bar(x=data.index, y=data['MACD_Histogram'], name='Гистограмма MACD'), row=3, col=1)

    # График объема торгов
    fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name='Объем'), row=4, col=1)

    fig.update_layout(title_text=f'Анализ акции {ticker} с {start_date} по {end_date}',
                      height=1200, width=1200)

    fig.show()

def calculate_and_display_average_price(data):
    """
    Вычисляет и выводит среднюю цену закрытия акций.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций, содержащий столбец 'Close'.

    Returns:
        float: Средняя цена закрытия акций.

    Prints:
        Выводит в консоль среднюю цену закрытия акций с двумя знаками после запятой.
    """
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия акций: {average_price:.2f}")
    return average_price
