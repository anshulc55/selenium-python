import pytest

def testMethod1():
    print("Hi, I am test Method 1")

@pytest.mark.skip("Skipping for Non Execution")
def testMethod2():
    print("Hi, I am test Method 2")

@pytest.mark.login
def testLoginUserName():
    print("Hi, I am testLoginUserName")

@pytest.mark.login
def testLoginPassword():
    print("Hi, I am testLoginPassword")

@pytest.mark.login
def testLoginInvalidCred():
    print("Hi, I am testLoginPassword")

@pytest.mark.login
def testLoginValidCred():
    print("Hi, I am testLoginValidCred")

@pytest.mark.login
def testLoginErrorMessage():
    print("Hi, I am testLoginErrorMessage")

@pytest.mark.login
def testLoginSuccessCase():
    print("Hi, I am testLoginSuccessCase")