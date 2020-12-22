from data_structures_and_algorithms_python.challenges.fizz_buzz_tree.fizz_buzz_tree import Node, BinaryTree, FizzOrBuzz, FizzBuzzTree 
import pytest

"""
Test Cases:
1. Can Successfully create a new fizzBuzz Tree.
2. Can successfully return empty tree when implementing fizzBuzzTree on an empty tree, and raises and exception when trying to traverse through it.
"""


def test_fizzbuzz_not_empty():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    fbt = FizzBuzzTree(bt)
    assert fbt.preOrder() == ['Fizz', '-1', 'Buzz', 'Buzz', '7', 'Fizz']

def test_fizzbuzz_empty():
    bt = BinaryTree()
    fbt = FizzBuzzTree(bt)
    with pytest.raises(AttributeError):
        assert fbt.preOrder()

