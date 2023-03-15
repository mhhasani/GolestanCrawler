from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytesseract 
from PIL import Image
import urllib.request
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://golestan.iust.ac.ir/forms/authenticateuser/main.htm')
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.switch_to.frame(driver.find_element_by_name('Master'))
driver.switch_to.frame(driver.find_element_by_name('Form_Body'))
username = wait(driver, 5).until(EC.visibility_of_element_located((By.ID, "F80351")))
username.send_keys("99472104")
password = wait(driver, 5).until(EC.visibility_of_element_located((By.ID, "F80401")))
password.send_keys("0024846015")
captcha = wait(driver, 5).until(EC.visibility_of_element_located((By.ID, "F51701")))
image_of_captcha = driver.find_element_by_id("imgCaptcha").get_attribute("src")
# download image
urllib.request.urlretrieve(image_of_captcha, "captcha.png")
# read image
captcha_text = pytesseract.image_to_string(Image.open('captcha.png'))
captcha.send_keys(captcha_text)
print(captcha_text)



driver.switch_to.parent_frame()
# print(driver.page_source)
wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,"iframe")))
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.switch_to.frame(driver.find_element_by_name('Master'))
driver.switch_to.frame(driver.find_element_by_name('Form_Body'))
driver.find_element_by_css_selector('mbar.mbargt2').click()