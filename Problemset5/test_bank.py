from bank import value

# Test cases for the value function

def test_value_hello():
    assert value("Hello") == 0

def test_value_hello_case_insensitive():
    assert value("hElLo") == 0

def test_value_hello_with_spaces():
    assert value("  Hello  ") == 0

def test_value_h():
    assert value("h") == 20

def test_value_h_case_insensitive():
    assert value("H") == 20

def test_value_h_with_spaces():
    assert value("  h  ") == 20

def test_value_other_greeting():
    assert value("Bonjour") == 100

def test_value_empty_string():
    assert value("") == 100

if __name__ == "__main__":
    import pytest
    pytest.main()
