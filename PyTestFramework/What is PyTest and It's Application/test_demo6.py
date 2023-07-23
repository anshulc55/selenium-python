import pytest

@pytest.fixture(scope="module")
def setUp():
    global num1, num2
    num1 = int(input("Enter the Num 1: "))
    num2 = int(input("Enter the Num 2: "))
    yield
    print("Output : ", result)


class TestMathOpearationsAddition:
    def test_addition(self, setUp):
        global result
        result = num1 + num2

class TestMathOpearationSubstraction:
    def test_substraction(self, setUp):
        global result
        result = num1 - num2

class TestMathOpearationMultiplication:
    def test_multiplication(self, setUp):
        global result
        result = num1 * num2



