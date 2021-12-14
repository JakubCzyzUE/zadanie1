import cv2
import matplotlib as plt
import pytesseract
from PIL import Image

def GetTxtFromImgae(img_path:str):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    img = Image.open(img_path)
    print(pytesseract.image_to_string(img))


GetTxtFromImgae(r'C:\Users\jakub\Desktop\images\txt.jpg')
GetTxtFromImgae(r'C:\Users\jakub\Desktop\images\txt2.png')
GetTxtFromImgae(r'C:\Users\jakub\Desktop\images\txt5.jpg')
GetTxtFromImgae(r'C:\Users\jakub\Desktop\images\txt4.jpg')
GetTxtFromImgae(r'C:\Users\jakub\Desktop\images\txt6.jfif')