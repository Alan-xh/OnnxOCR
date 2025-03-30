import os
import subprocess
import random
from datetime import datetime

def take_screenshot(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = os.path.join(output_folder, f"screenshot{timestamp}.png")
    subprocess.run(['/usr/sbin/screencapture', '-i', output_file], \
    stdout=subprocess.PIPE,  # 可选：如果需要捕获标准输出    \
    stderr=subprocess.PIPE,  # 可选：如果需要捕获错误输出    \
    bufsize=0)  # 设置 bufsize 为 0 表示无缓冲)
    return output_file

if __name__ == '__main__':
    outfile = take_screenshot("./onnxocr/image")
    print(f"图片保存在{outfile}")