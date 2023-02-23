import os
import urllib
import unicodedata
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from datetime import datetime

options = webdriver.ChromeOptions()
# options.add_argument("headless")


driver = webdriver.Chrome(
    executable_path="./chromedriver.exe", options=options)


driver.get('https://www.youtube.com/@user-nx5bg7pj9b/videos')
driver.set_window_size(1500, 900)
time.sleep(0.5)
driver.implicitly_wait(5)

images = driver.find_elements(
    by=By.XPATH, value='//*[@id="thumbnail"]/yt-image/img')
img_url = []
time.sleep(0.5)
driver.implicitly_wait(5)

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)
time.sleep(0.5)
driver.implicitly_wait(5)

urllib.request.urlretrieve(img_url[0], 'recent' + ".jpg")
time.sleep(0.5)
