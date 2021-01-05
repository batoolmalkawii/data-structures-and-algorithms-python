from data_structures_and_algorithms_python.challenges.quick_sort.quick_sort import quick_sort

"""
Test Cases:
1. Apply quick sort on an empty list.
2. Apply quick sort on a sorted list.
3. Apply quick sort on a reversed list.
4. Apply quick sort on a nearly-sorted list.
5. Apply quick sort on a non-sorted list.
5. Apply quick sort on a list that includes unique cases.
"""

def test_quick_empty():
    assert quick_sort([], 0, len([])-1) == []

def test_quick_sorted():
    assert quick_sort([1,2,3,4,5], 0, len([1,2,3,4,5])-1) == [1,2,3,4,5]

def test_quick_reversed():
    assert quick_sort([5,4,3,2,1], 0, len([5,4,3,2,1])-1) == [1,2,3,4,5]

def test_quick_nearly_sorted():
    assert quick_sort([2,3,5,7,13,11], 0, len([2,3,5,7,13,11])-1) == [2,3,5,7,11,13]

def test_quick_non_sorted():
    assert quick_sort([8,4,23,42,16,15], 0, len([8,4,23,42,16,15])-1) == [4, 8, 15, 16, 23, 42]

def test_quick_unique():
    assert quick_sort([5,12,7,5,5,7], 0, len([5,12,7,5,5,7])-1) == [5,5,5,7,7,12]
