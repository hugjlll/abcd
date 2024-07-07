from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2 as cv
from IDidentify.ifui import Ui_Dialog
from ai.handwritten_signature import Handwritten
from ai.ID import ID

class IdentifyDialog(QDialog):
    def __init__(self):
        super().__init__()
        print("-------")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.image_path1 = 'data/hw.jpg'
        self.image_path2 = 'data/id.jpg'

        # 加载图片并显示
        self.load_and_show_images()


        self.ui.pushButton.clicked.connect(self.perform_text_recognition_and_match)

        # 执行文字识别和匹配
        # self.perform_text_recognition_and_match()

    def load_and_show_images(self):
        # 加载第一张图片
        pixmap1 = QPixmap(self.image_path1)
        self.ui.video1.setPixmap(pixmap1.scaled(self.ui.video1.size(), Qt.KeepAspectRatio))

        # 加载第二张图片
        pixmap2 = QPixmap(self.image_path2)
        self.ui.video2.setPixmap(pixmap2.scaled(self.ui.video2.size(), Qt.KeepAspectRatio))

    def perform_text_recognition_and_match(self):

        # 文字识别并匹配处理
        try:

            text1 = Handwritten(cv.imread(self.image_path1))
            print(text1)
            text2 = ID(cv.imread(self.image_path2))
            print(text2)

            # 更新界面上的匹配结果标签
            if text1 == text2:
                self.ui.label_2.setText("是")
            else:
                self.ui.label_2.setText("否")

        except Exception as e:
            QMessageBox.warning(self, "错误", f"文字识别失败：{str(e)}")
