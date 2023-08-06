import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = "https://en-gb.facebook.com/"
def test_seleniumWaits():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.maximize_window()
    driver.get(URL)
    driver.find_ele

    driver.find_element(By.XPATH, "//a[@role='button' and @data-testid='open-registration-form-button']").click()

    month = driver.find_element(By.ID, 'month')
    dropdown = Select(month)

    dropdown.select_by_index(3)
    time.sleep(4)

    dropdown.select_by_visible_text("May")
    time.sleep(4)

    dropdown.select_by_value("4")
    time.sleep(4)

    driver.quit()