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







