import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = "https://en-gb.facebook.com/"
def test_captureScreen():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.maximize_window()
    driver.get(URL)

    driver.find_element(By.XPATH, "//a[@role='button' and @data-testid='open-registration-form-button']").click()

    month = driver.find_element(By.ID, 'month')
    dropdown = Select(month)

    dropdown.select_by_index(8)
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
    driver.get_screenshot_as_file("screen_"+timestamp+".png")

    driver.quit()