import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://edition.cnn.com/"
def test_seleniumWaits():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(120)

    driver.get(URL)

    driver.quit()