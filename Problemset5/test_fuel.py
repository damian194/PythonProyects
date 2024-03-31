import pytest
from fuel import convert
from fuel import gauge

# Test cases for the convert function
def test_convert_valid_input():
    assert convert("3/4") == 75

def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_convert_numerator_greater_than_denominator():
    with pytest.raises(ValueError):
        convert("4/3")

def test_gauge_partial_tank():
    assert gauge(50) == "50%"

if __name__ == "__main__":
    pytest.main()

