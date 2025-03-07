'''TEST_VALIDATOR: module for testing behaviour of validator.py'''
# pylint: disable=unused-variable

import pytest
from validator import is_valid_word, is_scrabble_word


VALID_SCRABBLE = [
    "alfa", "bravo", "charlie", "delta", "echo", "foxtrot",
    "golfer", "hotel", "inhale", "juliennes", "kilo", "lima", "mike",
    "nothing", "oscillate", "papa", "queen", "romeo", "sierra",
    "tango", "uniform", "victor", "whiskey", "xylem", "yanked", "zucchetto"
]
INVALID_SCRABBLE = [
    "axxxxx", "bxxxxx", "cxxxxx", "dxxxxx", "exxxxx", "fxxxxx",
    "gxxxxx", "hxxxxx", "ixxxxx", "jxxxxx", "kxxxxx", "lxxxxx", "mxxxxx",
    "nxxxxx", "oxxxxx", "pxxxxx", "qxxxxx", "rxxxxx", "sxxxxx",
    "txxxxx", "uxxxxx", "vxxxx", "wxxxxx", "xxxxxx", "yxxxxx", "zxxxxx"
]
INVALID_WORD = [
    "As45", "56dQ", "hel lo", "joy_", "insane$", "?wow"
]
PALINDROMES = [
    "aha", "bob", "civic", "deed", "eve", "gig", "kayak", "level", "madam",
    "noon", "otto", "pip", "radar", "sagas", "tenet", "ulu", "vav", "wow", "yay"
]


# --- IS_VALID_WORD ---


@pytest.mark.parametrize("valid_word", VALID_SCRABBLE + INVALID_SCRABBLE)
def test_is_valid_word_valid(valid_word):
    '''Test valid words return true'''
    assert is_valid_word(valid_word) is True


@pytest.mark.parametrize("invalid_word", INVALID_WORD)
def test_is_valid_word_invalid(invalid_word):
    '''Test invalid words return false'''
    assert is_valid_word(invalid_word) is False


@pytest.mark.parametrize("valid_capitalised_word", map(lambda x: x.upper(), VALID_SCRABBLE))
def test_is_valid_word_capitalised(valid_capitalised_word):
    '''Test capitalised valid words return true'''
    assert is_valid_word(valid_capitalised_word) is True


# --- IS_SCRABBLE_WORD ---


@pytest.mark.parametrize("palindromes", PALINDROMES)
def test_is_scrabble_word_true_true(palindromes):
    '''Test palindromes return true for forwards and reversed'''
    assert is_scrabble_word(palindromes) == [True, True]


@pytest.mark.parametrize("invalid_scrabble", INVALID_SCRABBLE)
def test_is_scrabble_word_false_false(invalid_scrabble):
    '''Test invalid scrabbles return false for forwards and reversed'''
    assert is_scrabble_word(invalid_scrabble) == [False, False]


@pytest.mark.parametrize("valid_forwards", VALID_SCRABBLE)
def test_is_scrabble_word_true_false(valid_forwards):
    '''Test invalid scrabble words return true forwards and false backwards'''
    assert is_scrabble_word(valid_forwards) == [True, False]


@pytest.mark.parametrize("valid_reversed", map(lambda x: x[::-1], VALID_SCRABBLE))
def test_is_scrabble_word_false_true(valid_reversed):
    '''Test invalid scrabble words return true forwards and false backwards'''
    assert is_scrabble_word(valid_reversed) == [False, True]
