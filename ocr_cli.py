#!/Users/xiaohui/opt/anaconda3/envs/cv/bin/python

import os
import cv2
import argparse
from onnxocr.onnx_paddleocr import ONNXPaddleOcr

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

parser = argparse.ArgumentParser()
parser.add_argument("--path", type=str, help='The path to the image file')
parser.add_argument("--file", type=str, default='1.png', help='The name of the image file')

args = parser.parse_args()


class OCRer:
    def __init__(self):
        self.model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)

    def ocr(self, filename):
        img = cv2.imread(filename)
        ocr_result = self.model.ocr(img)
        return ocr_result

    def ocr_print(self, filename):
        ocr_result = self.ocr(filename)
        result = []
        for box in ocr_result[0]:
            result.append(box[1][0])
        return result

if args.file:
    args.path = f"/Users/xiaohui/Desktop/{args.file}"

ocr = OCRer()
result = ocr.ocr_print(args.path)

for res in result:
    print(res)


