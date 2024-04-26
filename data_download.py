import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    """
        Функция для загрузки данных о биржевых запасах.

        Параметры:
            ticker (str): Тикер акции.
            period (str, опционально): Период времени для загрузки данных (по умолчанию '1mo' - один месяц).

        Возвращает:
            pd.DataFrame: DataFrame с данными о биржевых запасах.

        Function for downloading stock data.

        Parameters:
            ticker (str): The ticker of the promotion.
            period (str, optional): The time period for uploading data (by default, '1mo' is one month).

        Returns:
            pd.DataFrame: DataFrame with stock data.
     """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
        Функция для добавления скользящей средней к данным о биржевых акциях.

        Параметры:
            data (pd.DataFrame): DataFrame с данными о биржевых акциях.
            window_size (int, опционально): Размер окна для вычисления скользящей средней (по умолчанию 5).

        Возвращает:
            pd.DataFrame: DataFrame с добавленным столбцом скользящей средней.

        A function for adding a moving average to stock market data.

        Parameters:
            data (pd.DataFrame): A DataFrame with stock data.
            window_size (int, optional): The size of the window for calculating the moving average (default is 5).

        Returns:
            pd.DataFrame: DataFrame with the added moving average column.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
        Функция для вычисления и отображения средней цены закрытия акций.

        Параметры:
            data (pd.DataFrame): DataFrame с данными о биржевых акциях.

        Возвращает:
            None

        A function for calculating and displaying the average closing price of a stock.

        Parameters:
            data (pd.DataFrame): A DataFrame with stock data.

        Returns:
            None
    """
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия акций: {average_price}")


def notify_if_strong_fluctuations(data, threshold):
    """
        Функция для определения сильных колебаний цены акций и вывода уведомления.

        Параметры:
            data (pd.DataFrame): DataFrame с данными о биржевых акциях.
            threshold (float): Пороговое значение в процентах для определения сильных колебаний.

        Возвращает:
            None

        A function for detecting strong fluctuations in the share price and displaying a notification.

        Parameters:
            data (pd.DataFrame): A DataFrame with stock data.
            threshold (float): The threshold value in percentages for determining strong fluctuations.

        Returns:
            None
    """
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    range_price = max_price - min_price
    fluctuations_percentages = (range_price / min_price) * 100

    if fluctuations_percentages > threshold:
        print(f"Цена акций колебалась более чем на {threshold}% за период.")
    else:
        print("Цена акций не колебалась на заданный процент за период.")

def export_data_to_csv(data, filename):
    """
    Функция для экспорта данных о биржевых акциях в CSV файл.

    Параметры:
        data (pd.DataFrame): DataFrame с данными о биржевых акциях.
        filename (str): Имя файла для сохранения данных.

    Возвращает:
        None
    Function for exporting stock data to a CSV file.

     Parameters:
        data (pd.DataFrame): A DataFrame with stock data.
        filename (str): The name of the file to save the data.

     Returns:
        None
    """
    data.to_csv(filename, index=False)
    print(f"Создан файл с данными: {filename}")