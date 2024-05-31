import pickle
import os
import os.path as osp

# RGBD-Dataset
from .tartan import (TartanAir, TartanAirSample)


def dataset_factory(dataset_list, **kwargs):
    """ create a combined dataset """

    from torch.utils.data import ConcatDataset

    dataset_map = {
        'tartan': (TartanAir,),
        'tartan_sample': (TartanAirSample,),
    }

    db_list = []
    for key in dataset_list:
        # cache datasets for faster future loading
        db = dataset_map[key][0](**kwargs)

        print("Dataset {} has {} images".format(key, len(db)))
        db_list.append(db)

    return ConcatDataset(db_list)
