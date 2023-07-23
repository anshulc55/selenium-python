import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://classic.freecrm.com/"
def absoluteXpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    expected_title = "Free CRM - CRM software for customer relationship management, sales, and support."
    assert driver.title == expected_title

    driver.find_element(By.LINK_TEXT, "Sign Up").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div/div/div/a/img").click()
    time.sleep(5)
    assert driver.title == expected_title

    driver.quit()

def test_relativeXpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    expected_title = "Free CRM - CRM software for customer relationship management, sales, and support."
    assert driver.title == expected_title

    driver.find_element(By.LINK_TEXT, "Sign Up").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//a[@class='navbar-brand']/img[@class='img-responsive']").click()
    time.sleep(5)
    assert driver.title == expected_title

    driver.quit()
