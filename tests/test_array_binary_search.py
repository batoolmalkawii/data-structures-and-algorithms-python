from data_structures_and_algorithms_python.challenges.array_binary_search.array_binary_search import binarySearch

"""
Test Cases: 
1. [], 5 -> -1
2. [1, 2, 3, 4], 10 -> -1
3. [1, 2, 3, 4, 5, 6, 7, 8, 9], 7 -> 6
4. [1, 2, 3, 4, 5, 6, 7, 8, 9], 3 -> 2
"""

def test_bin_empty():
    actual = binarySearch([], 5)
    expected = -1
    assert actual == expected

def test_bin_not_in():
    actual = binarySearch([1, 2, 3, 4], 10)
    expected = -1
    assert actual == expected

def test_bin_in_low():
    actual = binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)
    expected = 6
    assert actual == expected

def test_bin_in_high():
    actual = binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    expected = 2
    assert actual == expected


