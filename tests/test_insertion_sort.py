from data_structures_and_algorithms_python.challenges.insertion_sort.insertion_sort import insertion_sort

"""
Test Cases:
1. Apply insertion sort on an empty list.
2. Apply insertion sort on a sorted list.
3. Apply insertion sort on a reversed list.
4. Apply insertion sort on a nearly-sorted list.
5. Apply insertion sort on a non-sorted list.
5. Apply insertion sort on a list that includes unique cases.
"""

def test_insertion_empty():
    assert insertion_sort([]) == []

def test_insertion_sorted():
    assert insertion_sort([1,2,3,4,5]) == [1,2,3,4,5]

def test_insertion_reversed():
    assert insertion_sort([5,4,3,2,1]) == [1,2,3,4,5]

def test_insertion_nearly_sorted():
    assert insertion_sort([2,3,5,7,13,11]) == [2,3,5,7,11,13]

def test_insertion_non_sorted():
    assert insertion_sort([8,4,23,42,16,15]) == [4, 8, 15, 16, 23, 42]

def test_insertion_unique():
    assert insertion_sort([5,12,7,5,5,7]) == [5,5,5,7,7,12]
