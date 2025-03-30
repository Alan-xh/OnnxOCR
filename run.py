from utility import take_screenshot
from test_ocr import OCRer
from onnxocr.onnx_paddleocr import ONNXPaddleOcr,sav2Img
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit, QMainWindow
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from datetime import datetime
import cv2
import sys
import os

current_path = os.getcwd()
parent_path = os.path.dirname(current_path)
os.chdir(parent_path)

class ScreenshotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        # 设置主窗口
        self.setWindowTitle('Screenshot App')
        self.setGeometry(100, 100, 800, 600)

        # 创建中央窗口部件
        central_widget = QWidget()        #模块依次为部件、布局、容器
        self.setCentralWidget(central_widget)

        # 创建主布局
        mainLayout = QHBoxLayout()

        # 创建左布局和右布局
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # 创建图片容器
        self.imageLabel = QLabel('Image will be displayed here')
        self.imageLabel.setAlignment(Qt.AlignCenter)  # 居中对齐
        left_layout.addWidget(self.imageLabel)

        # 创建按钮并添加到左侧布局底部
        self.screenshotButton = QPushButton('Take Screenshot')
        self.screenshotButton.clicked.connect(self.screenshot)  #触发截图
        left_layout.addWidget(self.screenshotButton)

        # 创建右侧文本容器
        self.textEdit = QTextEdit()
        self.textEdit.setPlaceholderText('Text will be displayed here')  #右文本框显示
        self.textEdit.setStyleSheet("""
                    QTextEdit {
                        padding: 10px;
                        text-align: center;
                        border: 1px solid gray;
                        border-radius: 5px;
                    }
                """)
        right_layout.addWidget(self.textEdit)

        # 将左侧和右侧布局添加到主布局
        mainLayout.addLayout(left_layout, stretch=1)
        mainLayout.addLayout(right_layout, stretch=1)

        # 设置中央窗口部件的布局
        central_widget.setLayout(mainLayout)



    def ocr(self, filename):  #输入待ocr的图片文件名，输出(img，识别结果,总用时)
        t1 = time.time()
        img = cv2.imread(filename)
        model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)
        ocr_result = model.ocr(img)
        t2 = time.time()
        total_time = "total time: {:.3f}".format(t2- t1)
        result = []
        for box in ocr_result[0]:
            result.append(box[1][0])
        return img, result, total_time


    def ocr_print(self, filename):  #输入待打印的文件，输出结果和总用时
        img, ocr_result, total_time = self.ocr(filename)
        print(ocr_result)
        print(total_time)
        result_list = []
        for box in ocr_result:
            result_list.append(box)
        result = "\n".join(result_list)
        res = f"{result} total time = {total_time}"
        return res


    def saveimg(self, filename, out_file):
        ret = self.ocr(filename)
        sav2Img(ret[0], ret[1], name = out_file)

    def screenshot(self):
        # 截取屏幕并保存
        input_image = take_screenshot("./onnxocr/image/")  #输入文件夹，输出文件路径
        result = self.ocr_print("./onnxocr/image/01.png")
        self.textEdit.setPlaceholderText(result)  # 右文本框显示
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        ocr_out = f'./onnxocr/outimage/outimg_{timestamp}.jpg'
        self.saveimg(input_image, ocr_out)

        # 将截图显示在图片容器中
        pixmap = QPixmap(ocr_out)
        self.imageLabel.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScreenshotApp()
    ex.show()
    sys.exit(app.exec_())
