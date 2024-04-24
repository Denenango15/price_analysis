import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия акций: {average_price}")


def notify_if_strong_fluctuations(data, threshold):
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    range_price = max_price - min_price
    fluctuations_percentages = (range_price / min_price) * 100

    if fluctuations_percentages > threshold:
        print(f"Цена акций колебалась более чем на {threshold}% за период.")
    else:
        print("Цена акций не колебалась на заданный процент за период.")
