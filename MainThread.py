import sys
from ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QStyle, QButtonGroup
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap, QImage
from Cache import Cache
from PyQt5.QtCore import QTimer
from loguru import logger
from DisplayThread import DisplayThread
from utils import ClsType, is_video_list_file_exists, load_cache_from_pkl


class MainThread(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("TEE-label")
        self.cache = Cache
        self.timer = QTimer()

        style = QApplication.style()
        import_folder = QtWidgets.QAction(
            style.standardIcon(QStyle.SP_FileIcon), "导入文件夹", self
        )
        import_file = QtWidgets.QAction(QIcon("ico.ico"), "导入文件", self)
        import_folder.triggered.connect(self.openFolder)
        import_file.triggered.connect(lambda: self.openFile(""))

        self.ui.menu.addAction(import_folder)
        self.ui.menu.addAction(import_file)

        self.show_video_thead = DisplayThread()

        self.ui.next_label.clicked.connect(self.next_onclicked)
        self.ui.prev_label.clicked.connect(self.prev_onclicked)

        self.radioButton_group = QButtonGroup()
        # 将11类别添加到同一按钮组中
        for i in range(11):
            self.radioButton_group.addButton(eval("self.ui.radioButton_" + str(i)), i)
        self.radioButton_group.addButton(self.ui.radioButton_None, -100)
        self.radioButton_group.addButton(self.ui.radioButton_others, -1)
        self.ui.radioButton_None.setVisible(False)
        self.radioButton_group.buttonClicked.connect(self.label)

        self.clsType = ClsType()

    def openFolder(self):
        foldername = QtWidgets.QFileDialog.getExistingDirectory(
            self, "打开文件夹", "./"
        )  # Qt 打开文件的函数
        self.opened_foldername = foldername
        if foldername != "":
            print(foldername)
            if not is_video_list_file_exists(foldername):
                self.cache.load_video_list_from_scratch(
                    self.cache, folder_path=foldername
                )
            else:
                logger.info("加载持久化数据")
                self.cache.load(
                    self.cache, load_cache_from_pkl(foldername + "/video_list.pkl")
                )
                self.cache.to_string(self.cache)
                # self.cache.load_video_list_from_json(self.cache, folder_path=foldername)
            if self.cache.video_count == 0:
                self.cache.pointer = -1
                logger.info("文件夹为空")
            else:
                self.openFile(self.cache.video_list[0][0])
            self.ui.pos_label.setText(
                f"{self.cache.pointer + 1} / {self.cache.video_count}"
            )
            label = self.cache.video_list[self.cache.pointer][1]
            eval(
                "self.ui.radioButton_"
                + f"{ClsType.translate(label)}"
                + ".setChecked(True)"
            )
            print(self.cache.video_list)

    def openFile(self, filename):
        if filename == "":
            filename = QtWidgets.QFileDialog.getOpenFileName(self, "打开文件", "./")[0]
            logger.info("选择文件")

        if filename != "":
            self.ui.filename_label.setText(filename.split("/")[-1])
            self.show_video_thead.selectfile(filename)
            logger.info("连接信号和槽")
            self.show_video_thead.show_frame_signal.connect(self.update_frame_label)
            logger.info("启动线程")
            self.show_video_thead.start()

    def update_frame_label(self, image):
        self.ui.display_label.setPixmap(QPixmap(image))

    def next_onclicked(self):
        cur = self.cache.pointer
        count = self.cache.video_count
        if cur < count - 1:
            self.cache.pointer += 1
            self.openFile(self.cache.video_list[self.cache.pointer][0])
            self.ui.pos_label.setText(
                f"{self.cache.pointer + 1} / {self.cache.video_count}"
            )
            label = self.cache.video_list[self.cache.pointer][1]
            eval(
                "self.ui.radioButton_"
                + f"{ClsType.translate(label)}"
                + ".setChecked(True)"
            )
        else:
            logger.info("已是最后一个视频")

    def prev_onclicked(self):
        cur = self.cache.pointer
        if cur > 0:
            self.cache.pointer -= 1
            self.openFile(self.cache.video_list[self.cache.pointer][0])
            self.ui.pos_label.setText(
                f"{self.cache.pointer + 1} / {self.cache.video_count}"
            )
            label = self.cache.video_list[self.cache.pointer][1]
            eval(
                "self.ui.radioButton_"
                + f"{ClsType.translate(label)}"
                + ".setChecked(True)"
            )
        else:
            logger.info("已是第一个视频")

    def label(self):
        checkedId = self.radioButton_group.checkedId()
        self.cache.video_list[self.cache.pointer][1] = str(checkedId)
        logger.info(self.cache.video_list)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        logger.info("关闭窗口")
        self.cache.flush(self.cache, self.opened_foldername)
        return super().closeEvent(a0)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    main_thread = MainThread()
    main_thread.show()
    sys.exit(myapp.exec_())
