import cv2
import time
<<<<<<< HEAD
from onnxocr.onnx_paddleocr import ONNXPaddleOcr,sav2Img
import sys
#固定到onnx路径·
# sys.path.append('./paddle_to_onnx/onnx')

model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)


img = cv2.imread('./onnxocr/test_images/1.jpg')
s = time.time()
result = model.ocr(img)
e = time.time()
print("total time: {:.3f}".format(e - s))
print("result:", result)
for box in result[0]:
    print(box)

sav2Img(img, result)
=======
from datetime import datetime
from onnxocr.onnx_paddleocr import ONNXPaddleOcr,sav2Img
import sys
#固定到onnx路径
# sys.path.append('./paddle_to_onnx/onnx')


class OCRer:
    def __init__(self):
        self.model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)

    def ocr(self, filename):
        t1 = time.time()
        img = cv2.imread(filename)
        ocr_result = self.model.ocr(img)
        t2 = time.time()
        total_time = "total time: {:.3f}".format(t2- t1)
        return img, ocr_result, total_time

    def ocr_print(self, filename):
        img, ocr_result, total_time = self.ocr(filename)
        result = []
        for box in ocr_result[0]:
            result.append(box[1][0])
        return result, total_time

    def saveimg(self, filename, out_file):
        ret = self.ocr(filename)
        sav2Img(ret[0], ret[1], name = out_file)



if __name__ == '__main__':
    ocr = OCRer()
    input_file = "./out_file/20241112"
    txt_file = "./text.txt"
    with open(txt_file, "a+") as f:
        for i in range(6):
            file_name = f"page_{i+1}.png"
            result, total_time = ocr.ocr_print(input_file+"/"+file_name)
            for res in result:
                f.write(res + "\n")
    print("已完成")


    # result = ocr.ocr_print("./onnxocr/image/01.png")
    # for i in result[0]:
    #     print(i)      #打印文本
    # print(result[1])  #打印总用时
    #
    # timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    # ocr_out = f'outimg_{timestamp}.jpg'
    # ocr.saveimg("./onnxocr/image/01.png", f"./onnxocr/outimage/{ocr_out}")
>>>>>>> 74123dc (renew)
