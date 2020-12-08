from data_structures_and_algorithms_python.data_structures.linked_list.linked_list import Node, LinkedList
import pytest


"""
Test cases - part 1:
    1. Can successfully instantiate an empty linked list.
        * list = LinkedList() -> None
    2. Can properly insert into the linked list.
        * list.insert(3) -> { 3 } -> NULL
    3. The head property will properly point to the first node in the linked list.
        * print (list.head.value) -> 3
    4. Can properly insert multiple nodes into the linked list.
        * list.insert(5)
        * list.insert(7)
        * list.insert(9)
    5. Will return true when finding a value within the linked list that exists.
        * list.includes(5) -> True
    6. Will return false when searching for a value in the linked list that does not exist.
        * list.includes(11) -> False
    7. Can properly return a collection of all the values that exist in the linked list.
        * print(list) -> "{ 9 } -> { 7 } -> { 5 } -> { 3 } -> NULL"
"""

def test_empty():
    list = LinkedList()
    assert list.head == None

def test_insert():
    list = LinkedList()
    list.insert(3)
    assert list.head.value == 3

def test_head():
    list = LinkedList()
    list.insert(3)
    assert list.head.value == 3

def test_insert_multi():
    list = LinkedList()
    list.insert(3)
    list.insert(5)
    list.insert(7)
    list.insert(9)
    assert list.head.value == 9
    assert list.head.next.value == 7
    assert list.head.next.next.value == 5
    assert list.head.next.next.next.value == 3
    assert list.head.next.next.next.next == None

def test_includes_true():
    list = LinkedList()
    list.insert(7)
    list.insert(9)
    assert list.includes(9) == True

def test_includes_false():
    list = LinkedList()
    list.insert(7)
    list.insert(9)
    assert list.includes(5) == False

def test_str():
    list = LinkedList()
    list.insert(3)
    list.insert(5)
    list.insert(7)
    list.insert(9)
    assert list.__str__() == "{ 9 } -> { 7 } -> { 5 } -> { 3 } -> NULL"

##########################################################################################
"""
Test cases - part 2:
    1. Can successfully add a node to the end of the linked list.
    2. Can successfully add multiple nodes to the end of a linked list.
    3. Can successfully insert a node before a node located i the middle of a linked list.
    4. Can successfully insert a node before the first node of a linked list.
    5. Can successfully insert after a node in the middle of the linked list.
    6. Can successfully insert a node after the last node of the linked list.
    7. Can successfully delete a value in the middle of the linked list.
    8. Can successfully delete a the first value of the linked list.
    9. Can successfully delete a the last value of the linked list.
"""

def test_append_empty():
    list = LinkedList()
    list.append(1)
    assert list.head.value == 1

def test_append():
     list = LinkedList()
     list.insert(1)
     list.insert(2)
     list.append(3)
     assert list.head.next.next.value == 3

def test_append_multi():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    assert list.head.value == 1
    assert list.head.next.value == 2
    assert list.head.next.next.value == 3

def test_insert_before_middle():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.insertBefore(2, 2.5)
    assert list.head.next.value == 2.5

def test_insert_before_first():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.insertBefore(1, 1.5)
    assert list.head.value == 1.5

def test_insert_after_middle():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.insertAfter(2, 2.5)
    assert list.head.next.next.value == 2.5

def test_insert_after_last():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.insertAfter(3, 3.5)
    assert list.head.next.next.next.value == 3.5

def delete_middle():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.deleteValue(2)
    assert list.head.next.value == 3

def delete_first():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.deleteValue(1)
    assert list.head.value == 2

def delete_last():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.deleteValue(1)
    assert list.head.next.next.value == None

##########################################################################################
"""
Test cases - part 3, test get_kth_value when:
1. Where k is greater than the length of the linked list
2. Where k and the length of the list are the same
3. Where k is not a positive integer
4. Where the linked list is of a size 1
5. “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
"""

def test_kth_greater():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    with pytest.raises(Exception):
        assert list.get_kth_value(5)

def test_kth_same_length():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    with pytest.raises(Exception):
        assert list.get_kth_value(3)
 
def test_kth_negative():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    with pytest.raises(Exception):
        assert list.get_kth_value(-1)

def test_kth_size_one():
    list = LinkedList()
    list.append(1)
    assert list.get_kth_value(0) == 1

def test_kth_middle():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    assert list.get_kth_value(1) == 2
##########################################################################################
"""
Test cases - part 4, test zipLists when:
1. Where both lists are empty.
2. Where 1st list is empty.
3. Where 2nd list is empty.
4. Where both lists have the same length.
5. Where 1st fist is longer than the 2nd list.
6. Where 2nd list is longer than the 1st list.
"""

def test_zip_empty():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.zipLists(list2)
    assert list1.__str__() == "NULL"

def test_zip_1st_empty():
    list1 = LinkedList()
    list2 = LinkedList()
    list2.append(1)
    list2.append(2)
    list2.append(3)
    list1.zipLists(list2)
    assert list1.__str__() == "{ 1 } -> { 2 } -> { 3 } -> NULL"

def test_zip_2nd_empty():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.zipLists(list2)
    assert list1.__str__() == "{ 1 } -> { 2 } -> { 3 } -> NULL"

def test_zio_same_length():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2.append(4)
    list2.append(5)
    list2.append(6)
    list1.zipLists(list2)
    assert list1.__str__() == "{ 1 } -> { 4 } -> { 2 } -> { 5 } -> { 3 } -> { 6 } -> NULL"

def test_zio_1st_longer():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2.append(4)
    list2.append(5)
    list1.zipLists(list2)
    assert list1.__str__() == "{ 1 } -> { 4 } -> { 2 } -> { 5 } -> { 3 } -> NULL"

def test_zio_2nd_longer():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list2.append(4)
    list2.append(5)
    list1.zipLists(list2)
    assert list1.__str__() == "{ 1 } -> { 4 } -> { 5 } -> NULL"













