import cv2
import os
from loguru import logger
from utils import *
import pickle


class Cache:
    video_list = []
    pointer = 0
    video_count = 0

    def __init__(self) -> None:
        pass

    def load_video_list_from_scratch(self, folder_path):
        self.fresh(self)
        print(folder_path)
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                # label = get_file_label(filename)
                if get_video_type(filename) == None or filename == "label_info.pkl":
                    continue
                else:
                    self.video_list.append([folder_path + "/" + filename, -1, 0])
            break

        logger.info(f"video_list: {self.video_list}")
        self.video_count = len(self.video_list)
        self.pointer = 0

    def fresh(self):
        self.video_list = []
        self.frame_list = []
        self.pointer = 0
        self.video_count = 0

    def flush(self, opened_foldername):
        # for kv in self.video_list:
        #     file_path = kv[0]
        #     label = kv[1]
        #     quality = kv[2]
        #     parts = file_path.split("_cls")
        #     new_file_path = parts[0] + "_cls" + str(label)
        #     if quality != 0:
        #         new_file_path = new_file_path + ""
        #     kv[0] = new_file_path
        #     os.rename(file_path, new_file_path)
        #     logger.info(f"{file_path} -> {file_path}" + "_cls" + str(label))
        with open(opened_foldername + "/label_info.pkl", "wb") as f:
            pickle.dump((Cache.video_list, Cache.video_count, Cache.pointer), f)
        logger.info("flush完成, 程序退出")

    def load(self, tuple):
        print(tuple)
        self.video_count = tuple[1]
        self.video_list = tuple[0]
        self.pointer = tuple[2]

    def to_string(self):
        print(f"video_list: {self.video_list}")
        print(f"pointer: {self.pointer}")
        print(f"video_count:{self.video_count}")
