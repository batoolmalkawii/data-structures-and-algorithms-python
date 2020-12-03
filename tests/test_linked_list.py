from data_structures_and_algorithms_python.data_structures.linked_list.linked_list import Node, LinkedList
import pytest


"""
Test cases:
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



