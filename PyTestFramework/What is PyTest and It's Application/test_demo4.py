import  pytest

@pytest.fixture()
def setUp():
    global num1, num2
    num1 = int(input("Enter the Num 1: "))
    num2 = int(input("Enter the Num 2: "))
    yield
    print("Output : ", result)

def test_addition(setUp):
    global result
    result = num1 + num2

def test_multiplication(setUp):
    global result
    result = num1 * num2

def test_substraction(setUp):
    global result
    result = num1 - num2