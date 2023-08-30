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


def weather_in_month_report(avg_highest_temperature_value, avg_lowest_temperature_value,
                            avg_mean_humidity_value):  # Generating report for month

    return (f"Highest Average Temperature: {avg_highest_temperature_value}C\n"
            f"Lowest Average Temperature : {avg_lowest_temperature_value}C\n"
            f"Average Mean Humidity : {avg_mean_humidity_value}%"
            )


def weather_each_day_report(temp_data_each_day, bonus):
    days = []
    for index, day in temp_data_each_day.iterrows():
        day_max = round(day['Max TemperatureC'])
        day_max_date = day['PKT']
        day_min = round(day['Min TemperatureC'])
        day_min_date = day['PKT']
        days.append(bar_charts(day_max, day_max_date, day_min, day_min_date, bonus))

    return days


def bar_charts(day_max, day_max_date, day_min, day_min_date, bonus):
    # ANSI escape codes for text colors
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    chart1 = ''
    chart2 = ''
    for x in range(day_max):
        chart1 += '+'
    if day_min >= 0:
        for y in range(day_min):
            chart2 += '+'
    else:
        for y in range(day_min):
            chart2 += '-'

    # Checking to see if bonus task is to be displayed
    if bonus is False:
        day_max_info = RED + f"{day_max_date}  {chart1}  {day_max}C" + RESET
        day_min_info = BLUE + f"{day_min_date}  {chart2}  {day_min}C" + RESET

        return (f"{day_max_info}\n"
                f"{day_min_info}"
                )
    else:
        each_day_output = f'{day_max_date}  {BLUE}{chart2}{RESET} {RED}{chart1}{RESET} {BLUE}{day_min}C{RESET} - {RED}{day_max}{RESET}C '
        return each_day_output
