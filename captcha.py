# train all the images in the golestan_captcha folder
import cv2
import pytesseract
from PIL import Image
import os
import time
import random
import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# read all the images in the golestan_captcha folder
folder = 'golestan_captcha'
images = []


for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename))
    if img is not None:
        images.append(img)
    
# convert images to grayscale
images_gray = []    
for img in images:
    images_gray.append(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))


# convert images to binary
images_binary_inv = []
for img in images_gray:
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    images_binary_inv.append(thresh1)

# convert captcha images to text
captchas = []
for img in images_binary_inv:
    captchas.append(pytesseract.image_to_string(img))



