class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
    def insert(self, new_val):
        # Your code goes here
        # if not self.value:
        #     self.value = new_val
        #     return
        # Node(new_val) = Node(new_val)
        if (self.root == None):
            self.root = Node(new_val)
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (new_val < current.value):
                    current = current.left
                else:
                    current = current.right
            if (new_val < parent.value):
                parent.left= Node(new_val)
            else:
                parent.right = Node(new_val)

    def printSelf(self):
        # Your code goes here
        print(self.root)

        
    def search(self, find_val):
        # Your code goes here
        while self.root!=None:
            if self.root.value == find_val:
                return True 
            if self.root.value < find_val:
                self.root = self.root.right
            else:
                self.root = self.root.left
        return False

tree = BST(4)

# print(tree.search(5))
print(tree.insert(2))
tree.insert(1)
tree.insert(3)
tree.insert(5)
