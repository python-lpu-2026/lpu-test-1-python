from solution import is_palindrome, second_largest, word_frequency

# -------- Q1 Tests --------
def test_palindrome_basic():
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False

def test_palindrome_case():
    assert is_palindrome("RaceCar") is True
    assert is_palindrome("") is True


# -------- Q2 Tests --------
def test_second_largest_basic():
    assert second_largest([10, 20, 30, 40]) == 30

def test_second_largest_duplicates():
    assert second_largest([5, 5, 5]) is None

def test_second_largest_negative():
    assert second_largest([-1, -2, -3]) == -2


# -------- Q3 Tests --------
def test_word_frequency_basic():
    assert word_frequency("Hello world hello") == {
        "hello": 2,
        "world": 1
    }

def test_word_frequency_empty():
    assert word_frequency("") == {}
