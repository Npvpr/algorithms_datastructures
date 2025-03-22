import visualize_tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, new_value):
        if not self.root:
            self.root = Node(new_value)
        else:
            self.insert_recursive(self.root, new_value)
        
    def insert_recursive(self, node, new_value):
        if node:
            pass

    def inorder_traversal(self, node):
        pass

