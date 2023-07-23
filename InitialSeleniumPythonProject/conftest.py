import pytest


@pytest.fixture()
def base_test():
    print("\nHi, This is Starting of Test Case .....")
    yield
    print("Hi, This is Ending of Test Case .....")
