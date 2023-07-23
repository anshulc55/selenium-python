import logging

import pytest
from InitialSeleniumPythonProject import dataprovider


@pytest.mark.usefixtures("base_test")
class TestLogin:
    # @pytest.mark.parametrize("username, password, browser", [("Anshul", "Anshul123", "chrome"), ("Mark", "Mark123", "IE"), ("Robert", "Robert123", "Firefox")])
    # def test_login(self, username, password, browser):
    #     print("Hi, I am in login Function")
    #     print(dataprovider.getData(username, password, browser))

    @pytest.mark.parametrize("argsValues", dataprovider.getData3("test1"))
    def test_login1(self, argsValues):
        #print("Hi, I am in login Function")
        #print(argsValues)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info("Hi, I am in login Function")
        logger.info(argsValues)

    @pytest.mark.parametrize("argsValues", dataprovider.getData3("test2"))
    def test_login2(self, argsValues):
        # print("Hi, I am in login Function")
        # print(argsValues)
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        logger.error("Hi, I am in login Function")
        logger.error(argsValues)
