import data_download as dd
import data_plotting as dplt

def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input("Введите период для данных (например, '1mo' для одного месяца), или нажмите Enter, чтобы установить произвольную дату: ")

    start_date = input(
        "Введите начальную дату в формате 'ГГГГ-ММ-ДД' (например, '2023-01-01'), или нажмите Enter для использования предустановленного периода: ")
    end_date = input(
        "Введите конечную дату в формате 'ГГГГ-ММ-ДД' (например, '2023-12-31'), или нажмите Enter для использования предустановленного периода: ")

    if start_date and end_date:  # Если даты начала и окончания указаны
        stock_data = dd.fetch_stock_data(ticker, start_date=start_date, end_date=end_date)
    else:
        stock_data = dd.fetch_stock_data(ticker, period=period)

    if stock_data.empty:
        print("Данные не загружены. Проверьте введенные данные и повторите попытку.")
        return

    # Add moving average and standard deviation to the data
    stock_data = dd.add_moving_average(stock_data)
    stock_data['Standard_Deviation'] = dd.calculate_standard_deviation(stock_data)

    # Plot the data, RSI and MACD
    dplt.create_and_save_plots(stock_data, ticker, period)

    # Calculate and display average price
    dd.calculate_and_display_average_price(stock_data)

    # Notify if strong fluctuations
    threshold = 10
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Export data to csv
    filename = f"{ticker}_{period}_stock_data.csv"
    dd.export_data_to_csv(stock_data, filename)

if __name__ == "__main__":
    main()
