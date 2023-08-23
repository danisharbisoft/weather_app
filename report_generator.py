import datetime
import pandas as pd


def weather_in_year_report(highest_temp_data, highest_humidity_data, lowest_temp_data, lowest_humidity_data):
    # Getting information for the highest temperature
    highest_temp_reading = round(highest_temp_data['Max TemperatureC'])
    highest_temp_date = highest_temp_data['PKT']

    # Getting information for the highest humidity
    highest_humidity_reading = round(highest_humidity_data['Max Humidity'])
    highest_humidity_date = highest_humidity_data['PKT']

    # Getting information for the highest temperature
    lowest_temp_reading = round(lowest_temp_data['Min TemperatureC'])
    lowest_temp_date = lowest_temp_data['PKT']

    # Getting information for the highest humidity
    lowest_humidity_reading = round(lowest_humidity_data['Min Humidity'])
    lowest_humidity_date = lowest_humidity_data['PKT']

    return (f"Highest Temp: {highest_temp_reading}C on {highest_temp_date}\n"
            f"Lowest Temp: {lowest_temp_reading}C on {lowest_temp_date}\n"
            f"Highest Humidity: {highest_humidity_reading}% on {highest_humidity_date}\n"
            f"Lowest Humidity: {lowest_humidity_reading}% on {lowest_humidity_date}"

            )


def weather_in_month_report(avg_highest_temperature_value, avg_lowest_temperature_value, avg_mean_humidity_value):
    pass


def weather_each_day_report():
    pass
