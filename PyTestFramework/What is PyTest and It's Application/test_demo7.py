import pytest

def test_first():
    print("I am test First")

def test_two():
    print("I am test Two")

@pytest.mark.order(1)
def test_three():
    print("I am test Three")


@pytest.mark.order(3)
def test_four():
    print("I am test Four")

@pytest.mark.order(2)
def test_five():
    print("I am test Five")
