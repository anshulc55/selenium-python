import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = "https://www.lambdatest.com/selenium-playground/javascript-alert-box-demo"
def test_captureScreen():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    driver.maximize_window
    driver.get(URL)

    driver.find_element(By.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div[1]/p/button').click()
    time.sleep(2)
    alert = Alert(driver)
    alert.accept()


    driver.find_element(By.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div[2]/div/p[1]/button').click()
    time.sleep(2)
    alert = Alert(driver)
    alert.dismiss()

    driver.quit()