from plates import is_valid  
import pytest

# Test valid plates
def test_valid_plate():
    assert is_valid("AB1234") == True

def test_valid_short_plate():
    assert is_valid("AB12") == True

# Test invalid plates
def test_invalid_length_plate():
    assert is_valid("ABC12345") == False

def test_invalid_format_plate():
    assert is_valid("1234AB") == False

# Additional test cases
def test_invalid_start_with_zero_plate():
    assert is_valid("AB0123") == False

def test_invalid_special_character_plate():
    assert is_valid("XY@456") == False

