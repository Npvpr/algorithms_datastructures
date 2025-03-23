import visualize_tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# All nodes on the left side must be smaller than the current/each node
# All nodes on the right side must be bigger than or equal to the current/each node
# Equal nodes are put to the right side of node (but here they are ignored)
# When deleting, replace current node with either smallest from the right side or largest from the left side
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, new_value):
        if not self.root:
            self.root = Node(new_value)
        else:
            self.insert_next(self.root, new_value)
    
    def insert_next(self, node, new_value):
        if new_value < node.value:
            if not node.left:
                node.left = Node(new_value)
            else:
                self.insert_next(node.left, new_value)
        elif new_value > node.value:
            if not node.right:
                node.right = Node(new_value)
            else:
                self.insert_next(node.right, new_value)
        else:
            # Don't add duplicates
            return
        
    # 1. Search deleting node(DN)
    #     1. compare with root
    #     2. compare with left
    #     3. compare with right
    # 2. Search smallest node(SN) on the right side of DN
    #     1. Compare with DN.right.left
    #     2. Keep going as far left as possible
    # 3. Replace SN with DN
    #     1. Get DN's parent, get if DN is left/right of parent
    #     2. SN.right = DN.right
    #     3. Set DN's parent's left/right to SN
    def delete(self, value):
        pass 

    def search(self, value):
        pass
    
    def inorder_traversal(self, node):
        pass

def insert_test():
    new_bt = BinarySearchTree()
    new_bt.insert(5)
    new_bt.insert(9)
    new_bt.insert(6)
    new_bt.insert(2)
    new_bt.insert(3)
    new_bt.insert(8)
    new_bt.insert(5)
    new_bt.insert(4)
    visualize_tree.plot_hierarchical_tree(new_bt.root)

def delete_test():
    pass

insert_test()