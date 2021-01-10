# Repeated Words

## Challenge
Write a function that accepts a lengthy string parameter without utilizing any of the built-in library methods available in Python, return the first word to occur more than once in that provided string.

## Approach & Efficiency
Approach: first, I removed the punctuation marks from the string so it does not affect the result, then converted it to lowercase.Then, I iterated through the words of string and initialized the word count to `0`. Then, I iterated through the words of the string and incremented the count of each word, when a word is repeated, it is returned.
Complexity: ***O(n)***, where n is the number of words in the string.

## User acceptance
Test Cases: `repeated_words`
1. Find the first word that occurs more than once in a string.
2. Find the first word that occurs more than once in a string that contains capital and small letters.
3. Find the first word that occurs more than once in a string that contains punctuation marks.
4. Return None when the given string has no repeated words.

Test Cases: `remove_punctuation`
1. Remove punctuation marks from a string.
2. Return the same string when it does not contain punctuation marks

