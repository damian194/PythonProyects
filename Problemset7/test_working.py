import pytest
from working import convert

# Define test cases
valid_test_cases = [
    ("1:30 PM to 2:45 PM", "13:30 to 14:45"),
    ("11:30 AM to 12:45 PM", "11:30 to 12:45"),
]

invalid_test_cases = [
    "1:30 to 2:45 PM",      # Missing 'AM' or 'PM'
    "1:30 PM to 14:45 PM",  # Invalid hour (14)
    "1:30 PM to 2:65 AM",   # Invalid minute (65)
    "15:30 PM to 2:45 AM",  # Invalid hour (15)
]

# Define test functions
@pytest.mark.parametrize("input_str, expected_output", valid_test_cases)
def test_valid_convert(input_str, expected_output):
    result = convert(input_str)
    assert result == expected_output

@pytest.mark.parametrize("invalid_input", invalid_test_cases)
def test_invalid_convert(invalid_input):
    with pytest.raises(ValueError):
        convert(invalid_input)

# Run the tests
if __name__ == "__main__":
    pytest.main()

