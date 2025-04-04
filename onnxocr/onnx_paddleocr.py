import time

<<<<<<< HEAD
from .predict_system import TextSystem
from .utils import infer_args as init_args
from .utils import str2bool, draw_ocr
import argparse
import sys
=======
from onnxocr.predict_system import TextSystem
from onnxocr.utils import infer_args as init_args
from onnxocr.utils import str2bool, draw_ocr
import argparse
>>>>>>> 74123dc (renew)


class ONNXPaddleOcr(TextSystem):
    def __init__(self, **kwargs):
<<<<<<< HEAD
        # 默认参数
=======
        # 默认参数，解析命令行参数，将这些参数的默认值存储到一个命名对象params中
>>>>>>> 74123dc (renew)
        parser = init_args()
        inference_args_dict = {}
        for action in parser._actions:
            inference_args_dict[action.dest] = action.default
        params = argparse.Namespace(**inference_args_dict)
<<<<<<< HEAD
=======
        
>>>>>>> 74123dc (renew)

        # params.rec_image_shape = "3, 32, 320"
        params.rec_image_shape = "3, 48, 320"

        # 根据传入的参数覆盖更新默认参数
        params.__dict__.update(**kwargs)

        # 初始化模型
        super().__init__(params)

    def ocr(self, img, det=True, rec=True, cls=True):
        if cls == True and self.use_angle_cls == False:
<<<<<<< HEAD
            print(
                "Since the angle classifier is not initialized, the angle classifier will not be uesd during the forward process"
            )
=======
            print('Since the angle classifier is not initialized, the angle classifier will not be uesd during the forward process')
>>>>>>> 74123dc (renew)

        if det and rec:
            ocr_res = []
            dt_boxes, rec_res = self.__call__(img, cls)
            tmp_res = [[box.tolist(), res] for box, res in zip(dt_boxes, rec_res)]
            ocr_res.append(tmp_res)
            return ocr_res
        elif det and not rec:
            ocr_res = []
            dt_boxes = self.text_detector(img)
            tmp_res = [box.tolist() for box in dt_boxes]
            ocr_res.append(tmp_res)
            return ocr_res
        else:
            ocr_res = []
            cls_res = []

            if not isinstance(img, list):
                img = [img]
            if self.use_angle_cls and cls:
                img, cls_res_tmp = self.text_classifier(img)
                if not rec:
                    cls_res.append(cls_res_tmp)
            rec_res = self.text_recognizer(img)
            ocr_res.append(rec_res)

            if not rec:
                return cls_res
            return ocr_res


def sav2Img(org_img, result, name="draw_ocr.jpg"):
    # 显示结果
    from PIL import Image
<<<<<<< HEAD

=======
>>>>>>> 74123dc (renew)
    result = result[0]
    # image = Image.open(img_path).convert('RGB')
    # 图像转BGR2RGB
    image = org_img[:, :, ::-1]
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores)
    im_show = Image.fromarray(im_show)
    im_show.save(name)


<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 74123dc (renew)
    import cv2

    model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)

<<<<<<< HEAD
    img = cv2.imread(
        "/data2/liujingsong3/fiber_box/test/img/20230531230052008263304.jpg"
    )
=======

    img = cv2.imread('/data2/liujingsong3/fiber_box/test/img/20230531230052008263304.jpg')
>>>>>>> 74123dc (renew)
    s = time.time()
    result = model.ocr(img)
    e = time.time()
    print("total time: {:.3f}".format(e - s))
    print("result:", result)
    for box in result[0]:
        print(box)

<<<<<<< HEAD
    sav2Img(img, result)
=======
    sav2Img(img, result)
>>>>>>> 74123dc (renew)
