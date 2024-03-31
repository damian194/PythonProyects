from twttr import shorten

# Test cases for the shorten function

def test_shorten_no_vowels():
    assert shorten("hello") == "hll"

def test_shorten_with_vowels():
    assert shorten("Python") == "Pythn"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_all_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_shorten_mixed_case():
    assert shorten("ApPlE") == "pPl"

def test_shorten_special_characters():
    assert shorten("123#@!&") == "123#@!&"

if __name__ == "__main__":
    import pytest
    pytest.main()
