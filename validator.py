'''VALIDATOR: Module for checking a word is valid.'''
# pylint: disable=unused-variable


def is_valid_word(passed_str: str) -> bool:
    """Checks whether a passed string is a valid word i.e. only alphabetic characters."""
    return passed_str.isalpha()


def is_scrabble_word(passed_word: str) -> list[bool]:
    """Checks whether the passed word is a scrabble word, both forwards and reversed."""
    passed_word = passed_word.lower()
    passed_word_reversed = passed_word[::-1]
    result = [False, False]
    with open("dictionary.txt", encoding="utf-8", mode="r") as dictionary:
        for line in dictionary:
            # strip word to remove new-line character
            word = line.strip()
            if word == passed_word:
                result[0] = True
            if word == passed_word_reversed:
                result[1] = True
            if all(result):
                return result
    return result
