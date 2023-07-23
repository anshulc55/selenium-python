import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://classic.freecrm.com/"
def FindElement():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    driver.find_element(By.CLASS_NAME, "form-control").send_keys("abc@gmail.com")
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "form-control").send_keys("passwordValue")
    time.sleep(5)

    driver.find_element(By.CLASS_NAME, "anshul123").send_keys("TestData")

    driver.quit()


def testFindElements():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    textElements = driver.find_elements(By.CLASS_NAME, "form-control")
    textElements[0].send_keys("abc@gmail.com")
    time.sleep(5)
    textElements[1].send_keys("passwordValue")
    time.sleep(5)

    dummy_textElements = driver.find_elements(By.CLASS_NAME, "dummy-control")
    print("Number of Web-Elemnts with class Dummy - ", len(dummy_textElements))

    driver.quit()

