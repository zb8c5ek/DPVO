__author__ = 'Xuanli CHEN'
"""
Xuanli Chen
Research Domain: Computer Vision, Machine Learning
Email: xuanli(dot)chen(at)icloud.com
LinkedIn: https://be.linkedin.com/in/xuanlichen
"""

import pickle
import numpy as np


def replace_path_and_verify(dict_in, folder_in):
    dict_out = {}


def check_match_scene_name(scene_name, dp_folder, scene_info):
    name = scene_name.split('/')[-3]
    p_number = scene_name.split('/')[-1]
    name_dp, p_dp = dp_folder.name.split('_sample_')
    if name == name_dp and p_number == p_dp:
        # Verify Using Poses
        dp_left_pose = np.loadtxt(dp_folder / p_dp / 'pose_left.txt')
        dp_right_pose = np.loadtxt(dp_folder / p_dp / 'pose_right.txt')
        poses = scene_info['poses']
        if np.allclose(poses, dp_left_pose):
            return True
        else:
            return False
    else:
        return False


def extract_matching_datasets(dp_tartan_sample, fp_pkl_in, fp_pkl_out):
    scene_info = pickle.load(open(fp_pkl_in, 'rb'))[0]
    scene_info_sample = {}
    LIST_dp_folders = [fp for fp in list(dp_tartan_sample.glob('*')) if fp.is_dir()]
    # --- 1. Parsing Using name and P number ---
    for scene_name, scene_info in scene_info.items():
        for dp_folder in LIST_dp_folders:
            if check_match_scene_name(scene_name, dp_folder, scene_info):
                print(scene_name, dp_folder)
                # replace_path_and_verify(dict_in=scene_info, folder_in=dp_folder)


if __name__ == '__main__':
    from pathlib import Path

    dp_tartan_sample = Path('/d_disk/Datasets/TartanAir').resolve()
    fp_pkl_in = Path('datasets/TartanAir.pickle').resolve()
    fp_pkl_out = Path('datasets/TartanAirSample.pickle').resolve()
    extract_matching_datasets(dp_tartan_sample, fp_pkl_in, fp_pkl_out)
