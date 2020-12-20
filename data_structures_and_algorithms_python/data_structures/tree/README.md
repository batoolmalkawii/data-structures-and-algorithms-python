# Trees

Ih this project, we created a data structure called **BinaryTree** and **BinarySearchTree** in Python. We used three classes, _Node_, _BinaryTree_, and _BinarySearchTree_.

**Node** included the following:

    1. `value`.
    2. `left`.
    3. `right`.

**BinaryTree** included the following:

    _Attributes_:
         1. `root`.

    _methods_:
        * a method for each of the depth first traversals called `preOrder`, `inOrder`, and `postOrder` which returns an array of the values, ordered appropriately.

**BinarySearchTree** -inherited from BinaryTree, included the following:

    _methods_:
       1. `add`: accepts a value, and adds a new node with that value in the correct location in the binary search tree.
       2. `contains`: accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.


**User acceptance tests** are included with the following test cases:

*BinaryTree* test cases:

    1. Can successfully instantiate an empty tree.
    2. Can successfully instantiate a tree with a single root node.
    3. Can successfully add a left child and right child to a single root node.
    4. Can successfully return a collection from a preorder traversal.
    5. Can successfully return a collection from an inorder traversal.
    6. Can successfully return a collection from a postorder traversal.
    7. Can successfully return the maximum value in the tree.
    8. Can successfully return an exception when we try to find the maximum value in an empty tree.

*BinarySearchTree* test cases:

    1. Can successfully instantiate an empty BST.
    2. Can successfully instantiate a tree with a single root node.
    3. Can successfully add multiple nodes to a BST.
    4. Can successfully return True when searching for an existing node in BST.
    5. Can successfully return False when searching for a non-existing node in BST.
    6. Can successfully raise an exception when searching in an empty BST.

