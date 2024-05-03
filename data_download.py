import yfinance as yf


def fetch_stock_data(ticker, start_date=None, end_date=None, period='1mo'):
    """
    Функция для загрузки данных о биржевых запасах.

    Параметры:
        ticker (str): Тикер акции.
        start_date (str, опционально): Начальная дата для загрузки данных (по умолчанию None).
        end_date (str, опционально): Конечная дата для загрузки данных (по умолчанию None).
        period (str, опционально): Период времени для загрузки данных (по умолчанию '1mo' - один месяц).

    Возвращает:
        pd.DataFrame: DataFrame с данными о биржевых запасах.
    """
    if start_date is not None and end_date is not None:
        data = yf.download(ticker, start=start_date, end=end_date, progress=False) # progress = True if your need notification about progress
    else:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
        Функция для добавления скользящего среднего к данным.

        Параметры:
            data (pd.DataFrame): DataFrame с данными о биржевых запасах.
            window_size (int, опционально): Размер окна для скользящего среднего (по умолчанию 5).

        Возвращает:
            pd.DataFrame: DataFrame с добавленным скользящим средним.
        """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_rsi(data, window=14):
    """
        Функция для вычисления индикатора RSI (индекс относительной силы).

        Параметры:
            data (pd.DataFrame): DataFrame с данными о биржевых запасах.
            window (int, опционально): Размер окна для вычисления RSI (по умолчанию 14).

        Возвращает:
            pd.Series: Столбец с значениями индикатора RSI.
        """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    """
        Функция для вычисления индикатора MACD (скользящее среднее сходимости/расхождения).

        Параметры:
            data (pd.DataFrame): DataFrame с данными о биржевых запасах.
            short_window (int, опционально): Короткий период окна для вычисления EMA (по умолчанию 12).
            long_window (int, опционально): Длинный период окна для вычисления EMA (по умолчанию 26).
            signal_window (int, опционально): Период окна для вычисления сигнальной линии (по умолчанию 9).

        Возвращает:
            pd.Series, pd.Series: Столбцы с значениями MACD и сигнальной линии.
        """
    short_ema = data['Close'].ewm(span=short_window, min_periods=1, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, min_periods=1, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_window, min_periods=1, adjust=False).mean()
    return macd_line, signal_line


def calculate_and_display_average_price(data):
    """
       Функция для вычисления и отображения средней цены закрытия акций.

       Параметры:
           data (pd.DataFrame): DataFrame с данными о биржевых запасах.
       """
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия акций: {average_price}")


def notify_if_strong_fluctuations(data, threshold):
    """
        Функция для уведомления о сильных колебаниях цены акций.

        Параметры:
            data (pd.DataFrame): DataFrame с данными о биржевых запасах.
            threshold (int): Пороговое значение процентных колебаний.

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
        Функция для экспорта данных в формат CSV.

        Параметры:
            data (pd.DataFrame): DataFrame с данными о биржевых запасах.
            filename (str): Имя файла для сохранения.

        """
    data.to_csv(filename, index=False)
    print(f"Создан файл с данными: {filename}")
