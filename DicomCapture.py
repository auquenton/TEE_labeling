import os
import SimpleITK as sitk
import numpy as np
import cv2

[x2, y2, x1, y1] = [430, 582, 62, 82]


class DicomCapture:
    def __init__(self, filename) -> None:
        dicom = sitk.ReadImage(filename)
        self.frames = np.squeeze(sitk.GetArrayFromImage(dicom))
        self.pointer = 0
        self.frames_count = self.frames.shape[0]
        print(self.frames.shape)

    def read(self):
        frame = self.frames[self.pointer]
        frame = frame[:, :, (2, 1, 0)]  # plt to cv
        frame = frame[y1:y2, x1:x2]
        self.pointer += 1
        return True, frame

    def get(self, flag):
        if flag == cv2.CAP_PROP_FRAME_COUNT:
            return self.frames_count
        return 0

    def set(self, flag, pos):
        if flag == cv2.CAP_PROP_POS_FRAMES:
            self.pointer = pos
