# FizzBuzzTree
`FizzBuzzTree` function is implemented.

## Challenge
Write a function called FizzBuzzTree which takes a k-ary tree as an argument.
Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

    If the value is divisible by 3, replace the value with “Fizz”
    If the value is divisible by 5, replace the value with “Buzz”
    If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    If the value is not divisible by 3 or 5, simply turn the number into a String.
Return a new tree.

## Approach
Approach: I used a **recursive** approach that walks through the elments of the tree, checks them if they are fizz or buzz or both. Then, adds the required value to the new treen 

## Solution
![Whiteboard](../../../assets/fizzbuzz_tree.png)


**User acceptance tests** are included with the following test cases:

Test Cases:
1. Can Successfully create a new fizzBuzz Tree.
2. Can successfully return empty tree when implementing fizzBuzzTree on an empty tree, and raises and exception when trying to traverse through it.

