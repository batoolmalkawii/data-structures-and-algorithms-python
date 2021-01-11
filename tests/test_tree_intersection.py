from data_structures_and_algorithms_python.challenges.tree_intersection.tree_intersection import tree_intersection, Node, BinaryTree
import pytest

"""
Test Cases:
1. Verify that the function will return the intersected elements between two lists.
2. Verify that the function will return an empty set if the two lists have no interstion.
3. Verify that the function will raise an exception if one of the trees is empty.
4. Verify that the function will return the same tree if we compared the tree with itself.
"""

def test_tree_inter_yes():
    bt = BinaryTree()
    bt2 = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    
    bt2.root = Node(6)
    bt2.root.right = Node(5)
    bt2.root.left = Node(1)
    bt2.root.right.left = Node(6)
    bt2.root.left.left = Node(10)
    bt2.root.right.right = Node(2)

    assert tree_intersection(bt, bt2) == {10, 5, 6}

def test_tree_inter_no():
    bt = BinaryTree()
    bt2 = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    
    bt2.root = Node(20)
    bt2.root.right = Node(30)
    bt2.root.left = Node(40)
    bt2.root.right.left = Node(50)
    bt2.root.left.left = Node(60)
    bt2.root.right.right = Node(70)

    assert tree_intersection(bt, bt2) == set()

def test_tree_inter_empty1():
    bt = BinaryTree()
    bt2 = BinaryTree()
   
    
    bt2.root = Node(20)
    bt2.root.right = Node(30)
    bt2.root.left = Node(40)
    bt2.root.right.left = Node(50)
    bt2.root.left.left = Node(60)
    bt2.root.right.right = Node(70)

    with pytest.raises(Exception):
        assert tree_intersection(bt, bt2)

def test_tree_inter_empty_both():
    bt = BinaryTree()
    bt2 = BinaryTree()

    with pytest.raises(Exception):
        assert tree_intersection(bt, bt2)

def test_tree_inter_same():
    bt = BinaryTree()   
    
    bt.root = Node(20)
    bt.root.right = Node(30)
    bt.root.left = Node(40)
    bt.root.right.left = Node(50)
    bt.root.left.left = Node(60)
    bt.root.right.right = Node(70)

    assert tree_intersection(bt, bt) == {20, 30, 40, 50, 60, 70}