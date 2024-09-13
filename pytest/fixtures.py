import math
import pytest

@pytest.fixture
def input_value():
    input=8
    return input

def test_check_diff(input_value):
    assert 99-91==input_value

def test_check_square_root(input_value):
    assert input_value==math.sqrt(64)

