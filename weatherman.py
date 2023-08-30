import argparse
import sys
import weather_calculations
from data_formatter import main_conversion


def main():
    args: argparse.Namespace = parse_arguments()
    weather_data = main_conversion(args.data_dir)  # Getting the pandas dataframe
    if not weather_data.empty:
        try:
            if args.yearly_report:
                weather_calculations.weather_in_year(weather_data, args.yearly_report)
                print()
            if args.monthly_report:
                weather_calculations.weather_in_month(weather_data, args.monthly_report)
                print()
            if args.every_day_report:
                weather_calculations.weather_each_day(weather_data, args.every_day_report, bonus=False)
            if args.bonus_task:
                weather_calculations.weather_each_day(weather_data, args.bonus_task, bonus=True)

        except ValueError as ve:
            sys.stderr.write(f"Error: {ve}\n")

    else:
        sys.stderr.write("Error: The files are not in the specified directory!\n")


def parse_arguments():  # Defining Command LIne Operations
    parser = argparse.ArgumentParser(
        description="A weather app which takes in data(in the form of year/month) and passes results")

    parser.add_argument('data_dir', type=str, help='Path to the directory which has the files')
    parser.add_argument('-e', "--yearly_report", type=str,
                        help="For a given YEAR displays the highest and lowest values for temperature and humidity."
                             "INPUT SHOULD BE IN THE FORM OF: <YEAR>")
    parser.add_argument('-a', "--monthly_report", type=str,
                        help="For a given MONTH displays the highest and lowest average values for temperature and mean humidity."
                             "INPUT SHOULD BE IN THE FORM OF:<YEAR>/<MONTH> ")
    parser.add_argument('-c', "--every_day_report", type=str,
                        help="For a given MONTH displays the highest and lowest values for temperature for each day in the form of horizontal charts."
                             "INPUT SHOULD BE IN THE FORM OF:<YEAR>/<MONTH>")
    parser.add_argument('-b', '--bonus_task', type=str,
                        help='This is a bonus task chart format which displays a single chart for the highest and lowest temp'
                             'INPUT SHOULD BE IN THE FORM OF:<YEAR>/<MONTH>')
    return parser.parse_args()


if __name__ == '__main__':
    main()
