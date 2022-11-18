from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QImage
from loguru import logger
import cv2
from utils import get_video_type, VideoType
from DicomCapture import DicomCapture


class DisplayThread(QThread):

    show_frame_signal = pyqtSignal(object)

    def __init__(self) -> None:
        logger.info("线程初始化开始")
        super(DisplayThread, self).__init__()
        self.timer = QTimer()
        logger.info("线程初始化完成")

    def selectfile(self, filename):
        self.frame_counter = 0
        self.filename = filename
        filetype = get_video_type(filename)
        if filetype == VideoType.REG:
            self.capture = cv2.VideoCapture(filename)
        elif filetype == VideoType.DCOM:
            self.capture = DicomCapture(filename)

    def run(self):
        timer = QTimer()
        logger.info("线程开启")
        timer.timeout.connect(self.show_frame)
        # self.capture = cv2.VideoCapture(self.filename)
        # self.timer.start(33)
        timer.start(33)
        self.exec()

    def show_frame(self):
        ret, image = self.capture.read()
        self.frame_counter += 1
        if self.frame_counter == int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT)):
            logger.info("循环播放")
            self.frame_counter = 0
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        qimg = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        self.show_frame_signal.emit(qimg)
