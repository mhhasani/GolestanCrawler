# download captcha from https://golestan.iust.ac.ir/Forms/AuthenticateUser/captcha.aspx

import cv2
import pytesseract
from PIL import Image
import urllib.request
import os
import time
import random
import string

# download captchas from https://golestan.iust.ac.ir/Forms/AuthenticateUser/captcha.aspx
folder = 'golestan_captcha'
if not os.path.exists(folder):
    os.makedirs(folder)
for i in range(500):
    image_of_captcha = 'https://golestan.iust.ac.ir/Forms/AuthenticateUser/captcha.aspx'
    # download image
    urllib.request.urlretrieve(image_of_captcha, os.path.join(folder, f'captcha_{i}.png'))
    # wait for 1 second
    time.sleep(3)


    
    




        