__author__ = 'Xuanli CHEN'
"""
Xuanli Chen
Research Domain: Computer Vision, Machine Learning
Email: xuanli(dot)chen(at)icloud.com
LinkedIn: https://be.linkedin.com/in/xuanlichen
"""
import os
import zipfile
from tqdm import tqdm
from pathlib import Path
import shutil

"""
to download the data, one need to run the original Tartan Air tools.
"""

processed_list = [
    'abandonedfactory',
    'abandonedfactory_night',
    'amusement',
    'carwelding',
    'endofworld',
    'gascola',
    'hospital',
    'japanesealley',
    'neighborhood',
    'ocean',
    'office',
    'office2',
    'oldtown',
    'seasidetown',
    'seasonsforest',
    'seasonsforest_winter'
]


def extract_all_zip_files(folder_path):
    # List all files in the directory
    zip_files = [file for file in os.listdir(folder_path) if file.endswith('.zip')]
    for file_name in tqdm(zip_files, desc="Extracting zip files"):
        file_path = os.path.join(folder_path, file_name)
        # Create a directory with the same name as the zip file
        extract_dir = os.path.join(folder_path, os.path.splitext(file_name)[0])
        os.makedirs(extract_dir, exist_ok=True)
        # Extract the zip file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Get list of files in zip to calculate extraction progress
            all_files = zip_ref.infolist()
            for member in tqdm(all_files, desc=f'Extracting {file_name}', leave=False):
                zip_ref.extract(member, extract_dir)
        print(f'Extracted {file_name} to {extract_dir}')


def combine_images_and_depths_into_one_folder(dp_depth_and_image, dp_out):
    # 1. List all the first level folders and sort
    list_folders = sorted([folder for folder in dp_depth_and_image.iterdir() if folder.is_dir()])

    # 2. move the folders inside each folder into the names
    for folder in tqdm(list_folders, desc='Moving folders into the Deep Patch Format'):
        name_end = folder.name.find('Easy')
        if name_end == -1:
            name_end = folder.name.find('Hard')
        name_end -= 1
        if folder.name[:name_end] in processed_list:
            continue
        target_folder = dp_out / folder.name[:name_end]
        target_folder.mkdir(exist_ok=True, parents=True)
        for sub_folder in folder.iterdir():
            assert sub_folder.name == target_folder.name
            # i) Scene Name Folder
            for easy_hard_folder in sub_folder.iterdir():
                # ii) Easy or Hard
                if easy_hard_folder.is_dir():
                    target_easy_hard_folder = target_folder / easy_hard_folder.name
                    if target_easy_hard_folder.exists():
                        # Merge contents if the sub-folder already exists
                        # iii) P folder
                        for p_folder in easy_hard_folder.iterdir():
                            target_p_folder = target_easy_hard_folder / p_folder.name
                            for item_in_p in p_folder.iterdir():
                                if item_in_p.is_dir():
                                    shutil.copytree(item_in_p, target_p_folder / item_in_p.name, dirs_exist_ok=False)

                    else:
                        shutil.copytree(easy_hard_folder, target_easy_hard_folder)


def main_process(cmd_args):
    if cmd_args == 'extract':
        folder_path = Path(r'/e_disk/TartanAir').resolve()
        extract_all_zip_files(folder_path)
    elif cmd_args == 'combine':
        dp_depth_and_image = Path(r'/e_disk/TartanAirUnZip').resolve()
        dp_out = Path(r'/e_disk/TartanAir').resolve()
        combine_images_and_depths_into_one_folder(
            dp_depth_and_image=dp_depth_and_image,
            dp_out=dp_out
        )


if __name__ == '__main__':
    # cmd_arg = 'extract'
    cmd_arg = 'combine'
    main_process(cmd_arg)
