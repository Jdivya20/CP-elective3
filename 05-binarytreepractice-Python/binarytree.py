class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """
        Return True if the find_val is in the tree and False otherwise.
        """
        # Your code goes here
        # if find_val < self.value:
        #     if self.left is None:
        #         return True
        #     return self.left.search(find_val)
        # elif find_val > self.value:
        #     if self.right is None:
        #         return True
        #     return self.right.search(find_val)
        # else:
        #     return self.value
        # pass
        if find_val==self.value:
            return True
        else:
            return self.root.left.search(find_val)

    def print_tree(self):
        """
        Print out all tree nodes as they are visited in a pre-order traversal."""
        # Your code goes here
        if self.left:
            self.left.PrintTree()
        print( self.value)
        if self.right:
            self.right.PrintTree()

    def preorder_search(self, start, find_val):
        """
        Helper method - use this to create a recursive search solution.
        """
        # Your code goes here
        pass

    def preorder_print(self, start, traversal):
        """
        Helper method - use this to create a recursive print solution.
        """
        # Your code goes here
        pass
tree = BinaryTree(1)
tree.search(4)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.search(4)
tree.search(6)