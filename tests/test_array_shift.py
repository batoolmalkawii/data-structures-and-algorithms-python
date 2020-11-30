from data_structures_and_algorithms_python.challenges.array_shift.array_shift import insertShiftArray
from data_structures_and_algorithms_python.challenges.array_shift.array_shift import removeShiftArray

######################################

"""
*insertShiftArray* test cases:
    1. [], 9 -> [9]
    2. [2], 4 -> [2, 4]
    3. [2, 1, 6, 7], 20 -> [2, 1, 20, 6, 7]
    4. [10, 20, 30], 15 -> [10, 20, 15, 30]
    5. [1, 2, 3, 4], "hello" -> [1, 2, "hello", 3, 4]
"""

def test_ins_empty():
    actual = insertShiftArray([], 9)
    expected = [9]
    assert actual == expected

def test_ins_one():
    actual = insertShiftArray([2], 4)
    expected = [2, 4]
    assert actual == expected

def test_ins_even():
    actual = insertShiftArray([2, 1, 6, 7], 20)
    expected = [2, 1, 20, 6, 7]
    assert actual == expected

def test_ins_odd():
    actual = insertShiftArray([10, 20, 30], 15)
    expected = [10, 20, 15, 30]
    assert actual == expected

def test_ins_string():
    actual = insertShiftArray([1, 2, 3, 4], "hello")
    expected = [1, 2, "hello", 3, 4]
    assert actual == expected


######################################

"""
*removeShiftArray* test cases:
    1. []-> []
    2. [2] -> []
    3. [2, 1, 6, 7] -> [2, 1, 7]
    4. [10, 20, 30] -> [10, 30]
    5. [1, 2, "hello", 4], -> [1, 2, 4]
"""

def test_remv_empty():
    actual = removeShiftArray([])
    expected = []
    assert actual == expected

def test_remv_one():
    actual = removeShiftArray([2])
    expected = []
    assert actual == expected

def test_remv_even():
    actual = removeShiftArray([2, 1, 6, 7])
    expected = [2, 1, 7]
    assert actual == expected

def test_remv_odd():
    actual = removeShiftArray([10, 20, 30])
    expected = [10, 30]
    assert actual == expected

def test_remv_string():
    actual = removeShiftArray([1, 2, "hello", 4])
    expected = [1, 2, 4]
    assert actual == expected








