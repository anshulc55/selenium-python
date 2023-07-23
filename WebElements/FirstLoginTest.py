import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.rediff.com/"
pageTitle = "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
def test_Login():
    # Login rediff.com
    driver = webdriver.Chrome()
    driver.maximize_window()

    # User will open rediff.com
    driver.get(URL)

    # verify the page title
    actualTitle = driver.title
    assert actualTitle == pageTitle

    # Click SignIn link
    signInLink = driver.find_element(By.CLASS_NAME, "signin")
    signInLink.click()

    # Enter Username and password
    userName = driver.find_element(By.ID, "login1")
    userName.send_keys("abc@gmail.com")

    password = driver.find_element(By.ID, "password")
    password.send_keys("dummyValue")
    time.sleep(5)

    # Click Sign-In Button
    signInButton = driver.find_element(By.CLASS_NAME, "signinbtn")
    signInButton.click()
    time.sleep(5)