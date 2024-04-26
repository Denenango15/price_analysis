import data_download as dd
import data_plotting as dplt



def main():
    """
       Основная функция для получения данных о биржевых акциях, построения графика и анализа колебаний цен.
       The main function is to obtain data on stock exchanges, plotting and analyzing price fluctuations.
    """
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Fetch stock data / Получение данных
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data / Добавление скользящих средних
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data / Построение графика
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Calculate and display average price / Рассчет и отображение средней цены
    dd.calculate_and_display_average_price(stock_data)

    # notify_if_strong_fluctuations / Вызов функции для оповещения о сильных колебаниях
    threshold = 10  # change your num
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # export data to csv / сохранение файла в csv
    filename = "Your_file_name.csv"
    dd.export_data_to_csv(stock_data, filename)

if __name__ == "__main__":
    main()
