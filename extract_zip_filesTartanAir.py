__author__ = 'Xuanli CHEN'
"""
Xuanli Chen
Research Domain: Computer Vision, Machine Learning
Email: xuanli(dot)chen(at)icloud.com
LinkedIn: https://be.linkedin.com/in/xuanlichen
"""
import os
import zipfile

# Path to the folder containing the zip files


# Create a function to extract all zip files
def extract_all_zip_files(folder_path):
    # List all files in the directory
    for file_name in os.listdir(folder_path):
        # Check if the file is a zip file
        if file_name.endswith('.zip'):
            file_path = os.path.join(folder_path, file_name)
            # Create a directory with the same name as the zip file
            extract_dir = os.path.join(folder_path, os.path.splitext(file_name)[0])
            os.makedirs(extract_dir, exist_ok=True)
            # Extract the zip file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            print(f'Extracted {file_name} to {extract_dir}')


def move_folders_to_DPVO_routine(folder_path):
    # List all files in the directory
    pass


if __name__ == '__main__':
    folder_path = 'path/to/your/folder'
    extract_all_zip_files(folder_path)