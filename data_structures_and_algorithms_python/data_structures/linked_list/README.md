# Linked Lists

Ih this project, we created a data structure called **Singly-Linked-List** in Python. We used two classes, _Node_ and _LinkedList_.

**Node** included the following:

    1. `value`.
    2. `next`.

**LinkedList** included the following:

    _Attributes_:
         1. `head`.

    _methods_:
        1. `insert`: takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
        2. `includes`: takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
        3. `__str__`: returns a string representing all the values in the Linked List, formatted as: `"{ a } -> { b } -> { c } -> NULL"`

**User acceptance tests** are included with the following test cases:

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

