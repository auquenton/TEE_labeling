from loguru import logger
from enum import Enum
import os
import pickle


class VideoType(Enum):
    REG = 0
    DCOM = 1
    NULL = 2


class ClsType:
    cls_dict = {
        "": "None",
        "-1": "None",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "10",
        "11": "11",
        "12": "12",
    }

    @staticmethod
    def translate(label):
        return ClsType.cls_dict[label]


def get_video_type(file_path):
    if file_path == "":
        return VideoType.NULL
    try:
        suffix = file_path.split(
            "/")[-1][file_path.split("/")[-1].index(".") + 1:]
    except Exception as e:
        logger.info("文件无后缀名")
        return VideoType.DCOM
    if suffix == "mp4" or suffix == "avi":
        return VideoType.REG
    else:
        return None


def get_file_label(filename):
    parts = filename.split("cls")
    return "" if len(parts) == 1 else parts[1]


def is_video_list_file_exists(foldername):
    for root, dirs, files in os.walk(foldername):
        break
    return True if "label_info.pkl" in files else False


def load_cache_from_pkl(pkl_file):
    with open(pkl_file, "rb") as f:
        video_list, video_count, pointer = pickle.load(f)
        print(video_list)
        print(video_count)
        print(pointer)
    return video_list, video_count, pointer
