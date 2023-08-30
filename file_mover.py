import os
import shutil
import zipfile


def move_files(source_directory_path, target_directory_path):  # This function moves the files to the target directory
    try:
        file_list1 = os.listdir(source_directory_path)  # List of files

        if not os.listdir(target_directory_path):  # Checking if the directory is empty or not

            for file in file_list1:  # Moving the files
                source_file_path = os.path.join(source_directory_path, file)
                destination_file_path = os.path.join(target_directory_path, file)

                if file.endswith('.zip'):  # Checking if the files are zipped or not
                    with zipfile.ZipFile(source_file_path, 'r') as zip_ref:
                        zip_ref.extractall(target_directory_path)
                else:
                    shutil.move(source_file_path, destination_file_path)

            print('files moved to target directory')
        else:
            print('Files already in right directory')

        return os.listdir(target_directory_path)

    except FileNotFoundError:
        print('Source or target directory not found.')
    except PermissionError:
        print('Permission denied. Make sure you have the required permissions.')
    except Exception as e:
        print(f'An error occurred: {e}')
