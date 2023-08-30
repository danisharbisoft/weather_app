from report_generator import weather_in_year_report, weather_in_month_report, weather_each_day_report
import sys


def weather_in_year(weather_data, date):
    filtered_data = weather_data[weather_data['PKT'].dt.year == int(date)]  # Getting data for the year specified

    # Giving error if user doesnt give right year
    if filtered_data.empty:
        sys.stderr.write('Error:Data for the given year does not exist')
    # formatting datetime
    filtered_data.loc[:, 'PKT'] = filtered_data['PKT'].dt.strftime('%d %B')

    # Getting highest temperature and humidity values.
    highest_temperature_row = highest_weather_value(filtered_data, 'Max TemperatureC')
    highest_humidity_row = highest_weather_value(filtered_data, 'Max Humidity')

    # Getting lowest temperature sand humidity values
    lowest_temperature_row = lowest_weather_value(filtered_data, 'Min TemperatureC')
    lowest_humidity_row = lowest_weather_value(filtered_data, 'Min Humidity')

    # Generating report
    report = weather_in_year_report(highest_temperature_row, highest_humidity_row, lowest_temperature_row,
                                    lowest_humidity_row)
    print(report)


def weather_in_month(weather_data, date):
    year, month = map(int, date.split('/'))
    filtered_data = weather_data[(weather_data['PKT'].dt.year == year) & (weather_data['PKT'].dt.month == month)]

    # Giving error if user doesnt give right year
    if filtered_data.empty:
        sys.stderr.write('Error:Data for the given year/month does not exist')

    # Finding the average highest temperature
    avg_highest_temp = round(average(filtered_data, 'Max TemperatureC'))

    # Finding the lowest average temperature
    avg_lowest_temp = round(average(filtered_data, 'Min TemperatureC'))

    # Finding Average humidity
    avg_humidity = round(average(filtered_data, 'Mean Humidity'))

    # Generating report
    report = weather_in_month_report(avg_highest_temp, avg_lowest_temp, avg_humidity)

    print(report)


def weather_each_day(weather_data, date,bonus):
    # filtering the data for the required values
    year, month = map(int, date.split('/'))
    filtered_data = weather_data[(weather_data['PKT'].dt.year == year) & (weather_data['PKT'].dt.month == month)]

    # Giving error if user doesnt give right year
    if filtered_data.empty:
        sys.stderr.write('Error:Data for the given year/month does not exist')

    filtered_data = filtered_data[['PKT', 'Max TemperatureC', 'Min TemperatureC']]

    # formatting datetime
    filtered_data.loc[:, 'PKT'] = filtered_data['PKT'].dt.strftime('%d %B')

    # Generating report
    report = weather_each_day_report(filtered_data,bonus)

    # Printing report for each day
    for each_day in report:
        print(each_day)


def highest_weather_value(filtered_data, search_field):  # This function finds the highest value
    max_idx = filtered_data[search_field].idxmax()
    max_value_row = filtered_data.loc[max_idx]

    return max_value_row


def lowest_weather_value(filtered_data, search_field):  # This function finds the lowest value
    min_idx = filtered_data[search_field].idxmin()
    min_value_row = filtered_data.loc[min_idx]

    return min_value_row


def average(filtered_data, search_field):
    average_value = filtered_data[search_field].mean()
    return average_value
