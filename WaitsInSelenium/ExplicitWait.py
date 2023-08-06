import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "file:///Users/anshul/Downloads/ExplicitWait.html"
def test_seleniumWaits():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 15)

    driver.maximize_window()
    driver.get(URL)

    # driver.find_element(By.ID, 'alert').click()
    # wait.until(EC.alert_is_present())

    driver.find_element(By.ID, 'populate-text').click()
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME , 'target-text'), 'Selenium Webdriver'))

    driver.quit()