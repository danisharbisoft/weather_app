import os
import shutil


def move_files(source_directory_path, target_directory_path):  # This function moves the files to the target directory
    file_list1 = os.listdir(source_directory_path)  # List of files

    if not os.listdir(target_directory_path):  # Checking if the directory is empty or not
        for file in file_list1:  # Moving the files
            source_file_path = os.path.join(source_directory_path, file)
            destination_file_path = os.path.join(target_directory_path, file)
            shutil.move(source_file_path, destination_file_path)
            print('files moved to target directory')
    else:
        print('files already in right directory')

    return os.listdir(target_directory_path)
