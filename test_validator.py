# pylint: disable=unused-variable
'''Test api file'''
import pytest
from validator import is_valid_word, is_valid_scrabble_word


VALID_WORDS = ["alfa", "bravo", "charlie", "delta", "echo", "foxtrot",
               "golfer", "hotel", "inhale", "juliennes", "kilo", "lima", "mike",
               "novemdecillion", "oscillate", "papa", "queen", "romeo", "sierra",
               "tango", "uniform", "victor", "whiskey", "xanthan", "yanked", "zucchetto"]
INVALID_WORDS = ["axxxxx", "bxxxxx", "cxxxxx", "dxxxxx", "exxxxx", "fxxxxx",
                 "gxxxxx", "hxxxxx", "ixxxxx", "jxxxxx", "kxxxxx", "lxxxxx", "mxxxxx",
                 "nxxxxx", "oxxxxx", "pxxxxx", "qxxxxx", "rxxxxx", "sxxxxx",
                 "txxxxx", "uxxxxx", "vxxxx", "wxxxxx", "xxxxxx", "yxxxxx", "zxxxxx"]
VALID_WORDS_REVERSED = [word[::-1] for word in VALID_WORDS]
INVALID_WORDS_REVERSED = [word[::-1] for word in INVALID_WORDS]
INVALID_ARGUMENTS = ["1234", "ab473", "_387f?", "furf ",
                     "03[]", "@fvvrc", "az ajqoq", "ffefe\n", " "]
CAPITALISED_VALID_WORDS = [word.upper() for word in VALID_WORDS]


@pytest.mark.parametrize("valid_argument", VALID_WORDS + INVALID_WORDS + CAPITALISED_VALID_WORDS)
def test_valid_argument(valid_argument):
    '''Test valid argument return true'''
    assert is_valid_word(valid_argument) == True


@pytest.mark.parametrize("invalid_argument", INVALID_ARGUMENTS)
def test_invalid_argument(invalid_argument):
    '''Test invalid argument return false'''
    assert is_valid_word(invalid_argument) == False


@pytest.mark.parametrize("valid_word", VALID_WORDS)
def test_valid_word_no_reverse_returns_true(valid_word):
    '''Test valid word returns true (when not checking for reverse)'''
    assert is_valid_scrabble_word(valid_word, False) == True


@pytest.mark.parametrize("valid_word_reversed", VALID_WORDS_REVERSED)
def test_valid_word_reversed_no_reverse_returns_false(valid_word_reversed):
    '''Test valid words reversed returns false (when not checking for reverse)'''
    assert is_valid_scrabble_word(valid_word_reversed, False) == False


@pytest.mark.parametrize("invalid_word", INVALID_WORDS)
def test_invalid_word_no_reverse_returns_false(invalid_word):
    '''Test invalid word returns false (when not checking for reverse)'''
    assert is_valid_scrabble_word(invalid_word, False) == False


@pytest.mark.parametrize("valid_word_reversed", VALID_WORDS_REVERSED)
def test_valid_word_reversed_check_reverse_returns_true(valid_word_reversed):
    '''Test valid word reversed returns true (when checking for reverse)'''
    assert is_valid_scrabble_word(valid_word_reversed, True) == True


@pytest.mark.parametrize("invalid_word_reversed", INVALID_WORDS_REVERSED)
def test_invalid_word_reversed_check_reverse_returns_false(invalid_word_reversed):
    '''Test invalid word reversed returns false (when checking for reverse)'''
    assert is_valid_scrabble_word(invalid_word_reversed, True) == False


@pytest.mark.parametrize("capitalised_valid_word", CAPITALISED_VALID_WORDS)
def test_valid_word_capitalised_no_reverse_returns_true(capitalised_valid_word):
    '''Test invalid word reversed returns false (when checking for reverse)'''
    assert is_valid_scrabble_word(capitalised_valid_word, False) == True


@pytest.mark.parametrize("capitalised_valid_word", CAPITALISED_VALID_WORDS)
def test_valid_word_capitalised_check_reverse_returns_true(capitalised_valid_word):
    '''Test invalid word reversed returns false (when checking for reverse)'''
    assert is_valid_scrabble_word(capitalised_valid_word, True) == True
