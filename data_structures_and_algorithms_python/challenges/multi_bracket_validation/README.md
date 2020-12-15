# Multi-Brackets Validation

## Challenge
Write a function called `multi_brackets_validation` that takes a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced.

## Approach & Efficiency
Approach: I used a **for** loop that iterates through the characters of the input string. If the character is an open bracket, it adds it to a list. If it is a closing bracket, it deletes its corresponding opening bracket. 
The function returns `True` if the list is empty after iteration, else it returns `False`.
Complexity: ***O(n)***, where n is the number of characters in the string.

## User acceptance
Test Cases:
    1. {}	TRUE
    2. {}(){}	TRUE
    3. ()[[Extra Characters]]	TRUE
    4. (){}[[]]	TRUE
    5. {}{Code}[Fellows](())	TRUE
    6. [({}]	FALSE
    7. (](	FALSE
    8. {(})	FALSE

