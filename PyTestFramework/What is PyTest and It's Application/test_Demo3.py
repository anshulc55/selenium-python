import pytest


def cal_rectangle_area(width, height):
    area = width * height
    return area


@pytest.mark.parametrize("a, b, expected_output", [(5, 5, 25), (10, 15, 150), (6, 5, 30), (100, 5, 500), (25, 15, 375)])
def test_area(a, b, expected_output):
    output = cal_rectangle_area(a, b)
    print(output)
    assert output == expected_output

# def test_area():
#     output = cal_rectangle_area(10, 21)
#     #assert - Actual Result --> Expected Result
#     assert output == 200
