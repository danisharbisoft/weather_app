import os
import pandas as pd


class DataProcessor:
    '''
    This class calls other classes and forms a list of the required data
    '''

    def __init__(self, target_directory_path, file_list_2, columns_to_read):
        self.target_directory_path = target_directory_path
        self.file_list_2 = file_list_2
        self.columns_to_read = columns_to_read

    def process_files(self):
        data_structure = []
        for file in self.file_list_2:
            file_extention = os.path.splitext(file)[1]
            destination_file_path = os.path.join(self.target_directory_path, file)

            try:
                data = FileReader(destination_file_path, file_extention, self.columns_to_read).read_and_process_data()

            except Exception as e:
                return f'Unexpected Error {e}'
            data_structure.append(data)
        return data_structure


class FileReader:
    '''
    This class reads eaxh file and filters data to the columns required
    '''

    def __init__(self, destination_file_path, file_extension, columns_to_read):
        self.destination_file_path = destination_file_path
        self.file_extension = file_extension
        self.columns_to_read = columns_to_read

    def read_and_process_data(self):
        if self.file_extension == '.txt':
            return self._process_txt()
        elif self.file_extension == '.tsv':
            return self._process_tsv()
        elif self.file_extension == '.xlsx':
            return self._process_excel()
        else:
            print(f"Unsupported file type: {self.file_extension}")
            return None

    def _process_txt(self, ):
        try:
            data = pd.read_csv(self.destination_file_path)
            data.columns = data.columns.str.strip()
            data = ConvertToDatetime(
                data).convert_column_to_datetime()  # Calling function from another class to convert PKT values to datetime
            data = data[self.columns_to_read]
            return data
        except pd.errors.EmptyDataError:
            return self._generate_error_message(self.destination_file_path, 'EmptyDataError')
        except pd.errors.ParserError:
            return self._generate_error_message(self.destination_file_path, 'EmptyDataError')

    def _process_tsv(self):
        try:
            data = pd.read_csv(self.destination_file_path, delimiter='\t')
            data.columns = data.columns.str.strip()
            data = ConvertToDatetime(
                data).convert_column_to_datetime()  # Calling function from another class to convert PKT values to datetime
            data = data[self.columns_to_read]
            return data
        except pd.errors.EmptyDataError:
            return self._generate_error_message(self.destination_file_path, 'EmptyDataError')
        except pd.errors.ParserError:
            return self._generate_error_message(self.destination_file_path, 'EmptyDataError')

    def _process_excel(self):
        try:
            data = pd.read_excel(self.destination_file_path)
            data.columns = data.columns.str.strip()
            data = ConvertToDatetime(
                data).convert_column_to_datetime()  # Calling function from another class to convert PKT values to datetime
            data = data[self.columns_to_read]
            return data

        except pd.errors.EmptyDataError:
            return self._generate_error_message(self.destination_file_path, 'EmptyDataError')

        except pd.errors.ParserError:
            return self._generate_error_message(self.destination_file_path, 'EmptyDataError')

    def _generate_error_message(self, destination_file_path, error_type):
        return f"{error_type} occurred while processing {destination_file_path}"


class ConvertToDatetime:
    def __init__(self, data):
        self.data = data

    def convert_column_to_datetime(self):
        '''
        :param data: Takes PKT Data as integer input.
        :return: Returns datetime format for PKT
        '''

        self.data['PKT'] = pd.to_datetime(self.data['PKT'])
        return self.data
