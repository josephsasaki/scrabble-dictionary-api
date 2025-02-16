

def is_valid_word(passed_str: str) -> bool:
    """Checks whether a passed string is a valid word i.e. only alphabetic characters."""
    return passed_str.isalpha()


def is_valid_scrabble_word(passed_word: str, check_reverse: bool) -> bool:
    """Checks whether the passed word is a valid scrabble word."""
    passed_word = passed_word.lower()
    passed_word_reversed = passed_word[::-1]
    with open("dictionary.txt", encoding="utf-8", mode="r") as f:
        if check_reverse:
            for line in f:
                if line.strip() in {passed_word, passed_word_reversed}:
                    return True
            return False
        for line in f:
            if line.strip() == passed_word:
                return True
        return False
