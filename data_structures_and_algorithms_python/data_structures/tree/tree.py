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


    def inOrder(self):
        output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            output.append(node.value)
            if node.right:
                _walk(node.right)
            return output

        if self.root:    
            _walk(self.root)
        else:
            raise AttributeError("Tree is empty.")

        return output

    def postOrder(self):
        output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            output.append(node.value)
            return output

        if self.root:    
            _walk(self.root)
        else:
            raise AttributeError("Tree is empty.")

        return output


    def findMaximumValue(self):
        if not self.root:
            raise AttributeError("Tree is empty.")

        max = self.root.value
        tree_elements = self.preOrder()

        for element in tree_elements:
            if element > max:
                max = element
        return (max)


    def breadthFirst(self):
        output = []
        visited = []

        if self.root:
            visited.append(self.root)
            output.append(self.root.value) #add root, level 1
        else:
            raise AttributeError("Tree is empty.")
            
        current = self.root

        # repeat for each level
        while current:
            if current.left:
                output.append(current.left.value) #add left
                visited.append(current.left)
            if current.right:
                output.append(current.right.value) #add right
                visited.append(current.right)
            visited.pop(0)
            if not visited:
                break
            current = visited[0]

        return (output)

    def maxinBT(self):
        if self.root == None:
            raise AttributeError("tree is empty")

        node = self.root

        def _walk(node):
            max = node.value
            left_max  = node.value
            right_max = node.value
           
            if node.left:
                left_max = _walk(node.left)
            if node.right:
                right_max = _walk(node.right)

            if (left_max > max):
                max = left_max
            if (right_max > max):
                max = right_max
            return max
        
        return (_walk(node))


    def mergerBTs(self, tree2):
        tree1 = self
        if tree1.root == None:
                        return tree2

        if tree2.root == None: 
                        return tree1

        node1 = tree1.root 
        node2 = tree2.root 

        def _merger(node1, node2):
                if node1 == None: 
                        return node2
                if node2 == None: 
                        return node1
                node1.value += node2.value 
                node1.Left = _merger(node1.left, node2.left)
                node1.right = _merger(node1.right, node2.right)
                return (node1) 

        _merger(node1, node2)
        return tree1.preOrder() 



"""BST"""
class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            def _walk(node):
                if value < node.value:
                    # go left
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        _walk(node.left)
                else:
                    # go right
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        _walk(node.right)
            _walk(self.root)

    def contains(self, value):
        if self.root == None:
            raise AttributeError("Tree is empty.")
        current = self.root
        while current:
            if current.value == value:
                return True
            if current.value > value:
                current = current.left
            else:
                current = current.right
        return False


    def doesContain(self, value):
        if self.root == None:
            return False
        node = self.root
        def _walk(node):
            if value == node.value:
                return True
            if value < node.value:
                if node.left:
                    _walk(node.left)
            else:
                if node.right:
                    _walk(node.right)
            return False

        return (_walk(node))

    def sumOfOddInBST(self):
        if self.root == None:
            raise AttributeError("tree is empty")
        
        node = self.root

        def _walk(node):
            if node == None:
                return 0
            if node.value % 2 != 0:
                return node.value + _walk(node.left) + _walk(node.right)
            if node.value % 2 == 0:
                return _walk(node.left) + _walk(node.right)

        return(_walk(node))







if __name__ == "__main__":

    """BT"""
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    bt2 = BinaryTree()
    bt2.root = Node(4)
    bt2.root.right = Node(1)
    bt2.root.left = Node(8)
    print("Pre-Order: ", bt.preOrder())
    print("In-Order: ", bt.inOrder())
    print("Post-Order: ", bt.postOrder())
    print("Maximum Value: ", bt.maxinBT())
    print ("BFS: ", bt.breadthFirst())
    print (bt.mergerBTs(bt2))

    """BST"""
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)
    print(bst.doesContain(4))
    print (bst.sumOfOddInBST())
    