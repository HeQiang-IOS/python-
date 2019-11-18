# coding = uft-8

import pytesseract
import subprocess
from PIL import Image
import os


os.chdir("/Users/heqiang/PycharmProjects/Python数据分析/爬虫")

def test1():
    image = Image.open('test.jpg')

    text = pytesseract.image_to_string(image)

    print(text)

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    # 对图片进行阈值过滤,然后保存
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)

    # 调用系统的tessercat命令对图片进行OCR识别
  #  subprocess.call(["cd /Users/heqiang/PycharmProjects/Python数据分析/爬虫/images", newFilePath, 'output'])

    # 打开文件读取结果
    file = open("output.txt", 'r')
    print(file.read())
    file.close()





if __name__ == "__main__":

    print(subprocess.check_output("ls /", shell=True))
    print(os.getcwd())
    print(subprocess.check_output("cd /Users/heqiang/PycharmProjects/Python数据分析/爬虫", shell=True))
    # cleanFile('tess2.jpg', 'text2clean.png')