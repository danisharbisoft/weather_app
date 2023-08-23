import os
import pandas as pd
from file_mover import move_files


def main_conversion(data_dir):
    source_directory = data_dir  # Path of the files in the computer
    target_directory = './raw_data'  # Directory where you want to move the files.
    target_files = move_files(source_directory, target_directory)
    combined_data_structure = format_files(target_directory, target_files)
    return combined_data_structure


def format_files(target_directory_path, file_list2):  # This function creates a pandas dataframe
    data_structure = []
    columns_to_read = ['PKT', 'Max TemperatureC', 'Mean TemperatureC', 'Min TemperatureC', 'Max Humidity',
                       'Mean Humidity', 'Min Humidity']
    data = None
    for file in file_list2:  # Going over each file in the new directory
        file_extention = os.path.splitext(file)[1]
        destination_file_path = os.path.join(target_directory_path, file)

        if file_extention == '.txt':  # Handles .txt files in the directory
            try:
                data = pd.read_csv(destination_file_path)
                data.columns = data.columns.str.strip()
                data = convert_to_datetime(data)  # Calling function to convert PKT values to datetime
                data = data[columns_to_read]

            except:
                print(f"The file causing problems is {file}")

        elif file_extention == '.tsv':  # Handles .tsv files in the directory
            try:
                data = pd.read_csv(destination_file_path, delimiter='\t')
                data.columns = data.columns.str.strip()
                data = convert_to_datetime(data)  # Calling function to convert PKT values to datetime
                data = data[columns_to_read]

            except:
                print(f"The  TSV file causing problems is {file}")

        elif file_extention == '.xlsx':  # Handles .xlsx files in the directory
            try:
                data = pd.read_excel(destination_file_path)
                data.columns = data.columns.str.strip()
                data = convert_to_datetime(data)  # Calling function to convert PKT values to datetime
                data = data[columns_to_read]
            except:
                print(f"The Excel file causing problems is {file}")

        data_structure.append(data)  # Adding the data toa single data structure
    combined_data = pd.concat(data_structure, ignore_index=True)
    combined_data.sort_values(by='PKT', inplace=True)
    return combined_data


def convert_to_datetime(data):  # Converts PKT values to datetime
    data['PKT'] = pd.to_datetime(data['PKT'])
    return data
