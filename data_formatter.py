import pandas as pd
from file_mover import move_files
from data_formatter_helper import DataProcessor


def main_conversion(data_dir):
    target_directory = './raw_data'  # Directory where you want to move the files.
    target_files = move_files(data_dir, target_directory)
    combined_data_structure = format_files(target_directory, target_files)
    return combined_data_structure


def format_files(target_directory_path, file_list2):  # This function creates a pandas dataframe
    columns_to_read = ['PKT', 'Max TemperatureC', 'Mean TemperatureC', 'Min TemperatureC', 'Max Humidity',
                       'Mean Humidity', 'Min Humidity']
    data_structure = DataProcessor(target_directory_path,file_list2,columns_to_read).process_files()

    combined_data = pd.concat(data_structure, ignore_index=True)
    combined_data.sort_values(by='PKT', inplace=True)
    return combined_data


def convert_to_datetime(data: int):
    '''

    :param data: Takes PKT Data as integer input.
    :return: Returns datetime format for PKT
    '''
    data['PKT'] = pd.to_datetime(data['PKT'])
    return data
