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
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """
        Print out all tree nodes as they are visited in a pre-order traversal."""
        # Your code goes here
        self.preorder_print(self.root)

    def preorder_search(self, start, find_val):
        """
        Helper method - use this to create a recursive search solution.
        """
        # Your code goes here
        if start == None:
            return False
        if start.value == find_val:
            return True
        else:
            return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)

    def preorder_print(self, start):
        """
        Helper method - use this to create a recursive print solution.
        """
        # Your code goes here
        if start is None:
            return
        print(start.value)
        self.preorder_print(start.left)
        self.preorder_print(start.right)
tree = BinaryTree(1)
tree.search(4)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.search(4)
tree.search(6)
tree.print_tree()