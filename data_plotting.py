import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None):
    """
        Функция для создания и сохранения графика цены акций с течением времени.

        Параметры:
            data (pd.DataFrame): DataFrame с данными о биржевых акциях.
            ticker (str): Тикер акции.
            period (str): Период времени для данных.
            filename (str, опционально): Имя файла для сохранения графика (по умолчанию None).

        Возвращает:
            None

        A function for creating and saving a stock price chart over time.

        Parameters:
            data (pd.DataFrame): A DataFrame with stock data.
            ticker (str): The ticker of the promotion.
            period (str): The time period for the data.
            filename (str, optional): The name of the file to save the graph (None by default).

        Returns:
            None
    """
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")



