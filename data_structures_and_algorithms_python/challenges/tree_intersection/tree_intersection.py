#from data_structures_and_algorithms_python.data_structures.tree.tree import BinaryTree

# A problem with import
"""Node"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""BT"""
class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self):
        output = []

        def _walk(node):
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        if self.root:    
            _walk(self.root)
        else:
            raise AttributeError("Tree is empty.")

        return output

"""------------------------------------------------------------------"""
def tree_intersection(tree1, tree2):
    if tree1.root == None or tree2.root == None:
        raise AttributeError("One of the trees is empty")
    else:
        tree1_set = set(tree1.preOrder())
        tree2_set = set(tree2.preOrder())
        return (tree1_set.intersection(tree2_set))
"""------------------------------------------------------------------"""

    
if __name__ == "__main__":
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
    
    print (tree_intersection(bt, bt2))

