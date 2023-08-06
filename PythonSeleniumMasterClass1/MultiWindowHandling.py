import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = "https://www.lambdatest.com/selenium-playground/window-popup-modal-demo"
def test_captureScreen():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    driver.maximize_window()
    driver.get(URL)
    print()
    print(driver.window_handles)

    driver.find_element(By.XPATH, "//a[@title='Follow @Lambdatesting on Twitter']").click()
    driver.switch_to.window(driver.window_handles[-1])
    print(driver.window_handles)
    print("Handles of Default and Twitter")
    time.sleep(5)
    driver.close()
    time.sleep(5)


    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, "//a[@title='Follow @Lambdatesting on Facebook']").click()
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)
    print(driver.window_handles)
    driver.close()
    time.sleep(5)


    driver.quit()
    # Close -- This will only close the Focus Window
    # Quite -- This will close the all windows including session