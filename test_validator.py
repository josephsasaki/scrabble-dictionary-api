# pylint: disable=unused-variable
'''Test api file'''
import pytest
from validator import is_valid_word, is_valid_scrabble_word


VALID_WORDS = ["alfa", "bravo", "charlie", "delta", "echo", "foxtrot",
               "golf", "hotel", "inhale", "juliennes", "kilo", "lima", "mike",
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
