import sys
from ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QStyle, QButtonGroup
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QIcon, QPixmap, QImage
from Cache import Cache
from PyQt5.QtCore import QTimer
from loguru import logger
from DisplayThread import DisplayThread
from utils import ClsType, is_video_list_file_exists, load_cache_from_pkl

# class Mouse_action(QtWidgets.QLabel):
#     def __init__(self,parent=None):
#         super(Mouse_action,self).__init__(parent)
        
#     def mousePress(self,event):
#         if event.buttons()==QtCore.Qt.LeftButton:
#             logger.info()
#         elif event.buttons()==QtCore.Qt.RightButton:
#             print("you")

class MainThread(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("TEE-label")
        self.cache = Cache
        self.timer = QTimer()
        # self.Mouse=Mouse_action()
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
        # self.ui.next_label.addAction()
        self.classify_group = QButtonGroup()
        # 将分类按钮添加到同一按钮组中
        for i in range(13):
            self.classify_group.addButton(eval("self.ui.radioButton_" + str(i)), i)
        self.classify_group.addButton(self.ui.radioButton_None, -1)
        self.ui.radioButton_None.setVisible(False)
        self.classify_group.buttonClicked.connect(self.label)
        
        self.qualify_group = QButtonGroup()
        self.qualify_group.addButton(self.ui.radioButton_good, 0)
        self.qualify_group.addButton(self.ui.radioButton_bad, 1)
        self.qualify_group.buttonClicked.connect(self.qualify)
        
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
                    self.cache, load_cache_from_pkl(foldername + "/label_info.pkl")
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
            if label == -1:
                label = "None"
            eval(
                "self.ui.radioButton_"
                + f"{str(label)}"
                + ".setChecked(True)"
            )
            quality = self.cache.video_list[self.cache.pointer][2]
            quality_str = "good" if quality == 0 else "bad"
            eval(
                "self.ui.radioButton_"
                + quality_str
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
            quality = self.cache.video_list[self.cache.pointer][2]
            if label == -1:
                label = "None"
            eval(
                "self.ui.radioButton_"
                + f"{str(label)}"
                + ".setChecked(True)"
            )
            quality_str = "good" if quality == 0 else "bad"
            eval(
                "self.ui.radioButton_"
                + quality_str
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
            quality = self.cache.video_list[self.cache.pointer][2]
            if label == -1:
                label = "None"
            eval(
                "self.ui.radioButton_"
                + f"{str(label)}"
                + ".setChecked(True)"
            )
            quality_str = "good" if quality == 0 else "bad"
            eval(
                "self.ui.radioButton_"
                + quality_str
                + ".setChecked(True)"
            )
        else:
            logger.info("已是第一个视频")

    def label(self):
        checkedId = self.classify_group.checkedId()
        if checkedId != -1:
            self.cache.video_list[self.cache.pointer][1] = checkedId
        logger.info(self.cache.video_list)
         
    def qualify(self):
        checkedId = self.qualify_group.checkedId()
        self.cache.video_list[self.cache.pointer][2] = checkedId
        logger.info(self.cache.video_list)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        logger.info("关闭窗口")
        self.cache.flush(self.cache, self.opened_foldername)
        return super().closeEvent(a0)
    
    def mousePressEvent(self,event):
        if event.button()==QtCore.Qt.LeftButton:
            self.prev_onclicked()
        elif event.button()==QtCore.Qt.RightButton:
            self.next_onclicked()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    main_thread = MainThread()
    main_thread.show()
    sys.exit(myapp.exec_())
