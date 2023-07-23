import pytest
from InitialSeleniumPythonProject import dataprovider
from InitialSeleniumPythonProject.logger import logClass


@pytest.mark.usefixtures("base_test")
class TestLogin(logClass):

    @pytest.mark.parametrize("argsValues", dataprovider.getData3("test1"))
    def test_login1(self, argsValues):
        #print("Hi, I am in login Function")
        #print(argsValues)
        self.info(argsValues)
        self.info("Hi, I am in login Function")



    @pytest.mark.parametrize("argsValues", dataprovider.getData3("test2"))
    def test_login2(self, argsValues):
        # print("Hi, I am in login Function")
        # print(argsValues)
        self.error(argsValues)
        self.critical("Hi, I am in login Function")


