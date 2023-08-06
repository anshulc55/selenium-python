import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = "https://in.freecrm.com/"

def test_checkBox():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.maximize_window()
    driver.get(URL)

    driver.find_element(By.XPATH, '//li/a[@href="https://register.freecrm.com/register/"]').click()

    checkBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    print()
    print("Number of CheckBoxes ", len(checkBoxes))

    #checkBoxes[0].click()
    time.sleep(3)

    print(checkBoxes[0].is_selected())

    driver.quit()

def radiobutton():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.maximize_window()
    driver.get(URL)

    driver.find_element(By.XPATH, "//a[@role='button' and @data-testid='open-registration-form-button']").click()

    radioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")
    print()
    print("Number of Radio Buttons", len(radioButtons))

    radioButtons[2].click()
    time.sleep(3)

    for i in range (1, len(radioButtons)):
        if radioButtons[i].is_selected() :
            print(radioButtons[i].text)
        else:
            print("No Radio Button is Selected by Default")

    driver.quit()