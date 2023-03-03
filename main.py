# crawl golestan website and save data in a csv file with selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


url = 'https://golestan.iust.ac.ir/forms/authenticateuser/main.htm'

driver = webdriver.Chrome()
driver.get(url)
# wait for finding CapRow id in the page
try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "F51701"))
    )
    print('F51701 found')

except:
    print('F51701 not found')
    # save source code of the page in a file
    with open('source.html', 'w') as f:
        f.write(driver.page_source)


