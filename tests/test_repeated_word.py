from data_structures_and_algorithms_python.challenges.repeated_word.repeated_word import repeared_word, remove_punctuation

"""
Test Cases: repeated_words
1. Find the first word that occurs more than once in a string.
2. Find the first word that occurs more than once in a string that contains capital and small letters.
3. Find the first word that occurs more than once in a string that contains punctuation marks.
4. Return None when the given string has no repeated words.

Test Cases: remove_punctuation
1. Remove punctuation marks from a string.
2. Return the same string when it does not contain punctuation marks
"""

def test_repeated_normal():
    assert repeared_word("Once upon a time there was a brave princess who") == "a"

def test_repeated_capital():
    assert repeared_word("Once upon A time there was a brave princess who") == "a"

def test_repeated_punc():
    assert repeared_word("Once upon a time, there was a brave princess who...") == "a"

def test_repeated_no_repeat():
    assert repeared_word("Once upon a time, there was brave princess who...") == None

def test_punc():
    assert remove_punctuation("Once upon a time, there was a brave princess who...") == "Once upon a time there was a brave princess who"

def test_punc_no():
    assert remove_punctuation("Once upon A time there was a brave princess who") == "Once upon A time there was a brave princess who"








