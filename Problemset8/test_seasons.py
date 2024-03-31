from datetime import date
import pytest
from seasons import is_leap_year

# Test is_leap_year function
def test_is_leap_year():
    # Test with known leap years
    assert is_leap_year(2000) == True
    assert is_leap_year(2004) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2022) == False

if __name__ == "__main__":
    pytest.main()





