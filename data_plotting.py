import matplotlib.pyplot as plt
import pandas as pd
from data_download import calculate_rsi, calculate_macd
import plotly.graph_objs as go


def create_and_save_plot(data, ticker, period, filename=None, style='ggplot'):
    """
    Функция для создания и сохранения графика цены акций с течением времени.

    Параметры:
        data (pd.DataFrame): DataFrame с данными о биржевых запасах.
        ticker (str): Тикер акции.
        period (str): Период времени для данных.
        filename (str, опционально): Имя файла для сохранения графика (по умолчанию None).
        style (str, опционально): Стиль оформления графика (по умолчанию 'ggplot'). В интерактивном не работает

    """
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
    fig.add_trace(go.Scatter(x=data.index, y=data['Moving_Average'], mode='lines', name='Moving Average'))

    fig.update_layout(title=f"{ticker} Цена акций с течением времени", xaxis_title="Дата", yaxis_title="Цена")

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.html"

    fig.write_html(filename)
    print(f"Интерактивный график сохранен как {filename}")

    '''if you don't need an interactive graph, then you need to remove the # from the code below'''

    # plt.figure(figsize=(10, 6))
    #
    # if 'Date' not in data:
    #     if pd.api.types.is_datetime64_any_dtype(data.index):
    #         dates = data.index.to_numpy()
    #         plt.plot(dates, data['Close'].values, label='Close Price')
    #         plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
    #         plt.fill_between(dates, data['Moving_Average'].values - 2 * data['Standard_Deviation'].values,
    #                          data['Moving_Average'].values + 2 * data['Standard_Deviation'].values, alpha=0.2)
    #     else:
    #         print("Информация о дате отсутствует или не имеет распознаваемого формата.")
    #         return
    # else:
    #     if not pd.api.types.is_datetime64_any_dtype(data['Date']):
    #         data['Date'] = pd.to_datetime(data['Date'])
    #     plt.plot(data['Date'], data['Close'], label='Close Price')
    #     plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
    #     plt.fill_between(data['Date'], data['Moving_Average'] - 2 * data['Standard_Deviation'],
    #                      data['Moving_Average'] + 2 * data['Standard_Deviation'], alpha=0.2)
    #
    # plt.title(f"{ticker} Цена акций с течением времени")
    # plt.xlabel("Дата")
    # plt.ylabel("Цена")
    # plt.style.use(style)  # Применение выбранного стиля
    # plt.legend()
    #
    # if filename is None:
    #     filename = f"{ticker}_{period}_stock_price_chart.png"
    #
    # plt.savefig(filename)
    # print(f"График сохранен как {filename}")



def plot_rsi(data, ticker, period, filename=None):
    """
        Функция для построения и сохранения графика индикатора RSI с течением времени.

        Параметры:
            data (pd.DataFrame): DataFrame с данными о биржевых запасах.
            ticker (str): Тикер акции.
            period (str): Период времени для данных.
            filename (str, опционально): Имя файла для сохранения графика (по умолчанию None).

        """
    rsi = calculate_rsi(data)
    plt.figure(figsize=(10, 4))
    plt.plot(data.index, rsi, label='RSI', color='blue')
    plt.title(f"{ticker} Индикатор RSI с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("RSI")
    plt.legend()
    if filename is None:
        filename = f"{ticker}_{period}_rsi_chart.png"
    plt.savefig(filename)
    print(f"График RSI сохранен как {filename}")


def plot_macd(data, ticker, period, filename=None):
    '''Функция создает и сохраняет график индикатора MACD с течением времени.
    Параметры:
    data (pd.DataFrame): DataFrame с данными о биржевых запасах.
    ticker (str): Тикер акции.
    period (str): Период времени.
    filename (str, опционально): Имя файла для сохранения графика (по умолчанию создается автоматически).
   '''
    macd_line, signal_line = calculate_macd(data)
    plt.figure(figsize=(10, 4))
    plt.plot(data.index, macd_line, label='MACD', color='blue')
    plt.plot(data.index, signal_line, label='Signal Line', color='red')
    plt.title(f"{ticker} Индикатор MACD с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("MACD")
    plt.legend()
    if filename is None:
        filename = f"{ticker}_{period}_macd_chart.png"
    plt.savefig(filename)
    print(f"График MACD сохранен как {filename}")


def create_and_save_plots(data, ticker, period):
    '''Функция вызывает другие функции для создания и сохранения графиков цены акций, RSI и MACD.
    Параметры:
    data (pd.DataFrame): DtaFrame с данными о биржевых запасах.
    ticker (str): Тикер акции.
    period (str): Период времени.
    '''
    create_and_save_plot(data, ticker, period)
    plot_rsi(data, ticker, period)
    plot_macd(data, ticker, period)
