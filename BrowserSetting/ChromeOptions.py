import time

from selenium import webdriver


def test_chromeOptions():
    #Chrome Options Class
    c_options = webdriver.ChromeOptions()
    c_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    c_options.add_experimental_option("useAutomationExtension", False)
    c_options.accept_insecure_certs = True
    c_options.add_argument("--window-size=1800,600")

    driver = webdriver.Chrome(options=c_options)
    #driver.maximize_window()
    driver.get("https://www.cacert.com")
    time.sleep(10)
    driver.quit()