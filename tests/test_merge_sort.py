from data_structures_and_algorithms_python.challenges.merge_sort.merge_sort import merge_sort

"""
Test Cases:
1. Apply merge sort on an empty list.
2. Apply merge sort on a sorted list.
3. Apply merge sort on a reversed list.
4. Apply merge sort on a nearly-sorted list.
5. Apply merge sort on a non-sorted list.
5. Apply merge sort on a list that includes unique cases.
"""

def test_merge_empty():
    assert merge_sort([]) == []

def test_merge_sorted():
    assert merge_sort([1,2,3,4,5]) == [1,2,3,4,5]

def test_merge_reversed():
    assert merge_sort([5,4,3,2,1]) == [1,2,3,4,5]

def test_merge_nearly_sorted():
    assert merge_sort([2,3,5,7,13,11]) == [2,3,5,7,11,13]

def test_merge_non_sorted():
    assert merge_sort([8,4,23,42,16,15]) == [4, 8, 15, 16, 23, 42]

def test_merge_unique():
    assert merge_sort([5,12,7,5,5,7]) == [5,5,5,7,7,12]
