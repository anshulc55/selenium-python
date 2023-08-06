import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.google.com/"
def test_seleniumWaits():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    searchBox = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    searchBox.send_keys("selenium-webdriver")

    time.sleep(5)
    driver.find_element(By.XPATH, '//div[@role="option" and @aria-label="selenium-webdriver github"]').click()

    driver.quit()