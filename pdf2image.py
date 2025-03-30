import os.path

import fitz  # PyMuPDF
from datetime import date
def pdf_to_images(pdf_path, output_dir):
    # 打开PDF文件
    pdf_document = fitz.open(pdf_path)

    # 获取页数
    num_pages = pdf_document.page_count
    time = date.today().strftime("%Y%m%d")
    # 遍历前8页
    for page_num in range(num_pages):
        page = pdf_document.load_page(page_num)  # 加载页面
        pix = page.get_pixmap()  # 获取页面像素图

        # 保存为图片
        image_path = f"{output_dir}/{time}"
        if not os.path.exists(image_path):
            os.mkdir(image_path)
        file_name = f"/page_{page_num + 1}.png"
        pix.save(image_path + file_name)
        print(f"Saved {image_path} + {file_name}")

pdf_path = "/Users/xiaohui/Downloads/英语答案-10月质量检测.pdf"
# 示例用法
pdf_to_images(pdf_path, "./out_file")

