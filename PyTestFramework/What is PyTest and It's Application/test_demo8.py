import pytest
import logging


def cal_rectangle_area(width, height):
    area = width * height
    return area


@pytest.mark.parametrize("a, b, expected_output", [(5, 5, 25), (10, 15, 150), (6, 5, 30), (100, 5, 500), (25, 15, 375)])
def test_area(a, b, expected_output):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info("Given Width is - {0}, and Height is -{1}. So Expected Area is - {2}".format(a, b, expected_output))
    output = cal_rectangle_area(a, b)
    print(output)
    assert output == expected_output

