import pytest


@pytest.fixture(scope="class")
def setUp():
    global num1, num2
    num1 = int(input("Enter the Num 1: "))
    num2 = int(input("Enter the Num 2: "))
    yield
    print("Output : ", result)


@pytest.mark.usefixtures("setUp")
class TestMathOpearationsAddition:
    def test_addition(self):
        global result
        result = num1 + num2

@pytest.mark.usefixtures("setUp")
class TestMathOpearationSubstraction:
    def test_substraction(self):
        global result
        result = num1 - num2

@pytest.mark.usefixtures("setUp")
class TestMathOpearationMultiplication:
    def test_multiplication(self):
        global result
        result = num1 * num2



