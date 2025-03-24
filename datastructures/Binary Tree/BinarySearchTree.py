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
        
    # Possile Deletes:
    #   1. Empty tree
    #   2. Delete root
    #   3. Delete node with no children
    #   4. Delete node with no left child
    #   5. Delete node with no right child
    #   6. Delete node doesn't exist in the tree
    # 1. Search deleting node(DN)
    #   1. compare with root
    #   2. compare with left
    #   3. compare with right
    # 2. If left side of DN is empty, search smallest node(SN) on the right side of DN
    #   1. Compare with DN.right.left
    #   2. Keep going as far left as possible
    # 2. If right side of DN is empty, search largest node(LN) on the left side of DN
    #   1. Compare with DN.left.right
    #   2. Keep going as far right as possible   
    # 3. Replace SN with DN
    #   1. Get DN's parent, get if DN is left/right of parent
    #   2. SN.right = DN.right
    #   3. Set DN's parent's left/right to SN
    # def delete(self, value):
    #     # If tree is empty
    #     # if not self.root:
    #     #     print("No nodes in the tree")
    #     #     return
        
    #     # cur_node = self.root
    #     # while(cur_node):
    #     #     if value < cur_node.value:
    #     #         cur_node = cur_node.left
    #     #     elif value > cur_node.value:
    #     #         cur_node = cur_node.right
    #     #     else:
    #     #         self.replace(cur_node, parent, value)
    #     pass

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        # Base case: If the tree is empty
        if node is None:
            return None
        
        # Navigate to the node to be deleted
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            # Instead of swapping values, we'll properly replace the node
            successor_parent = node
            successor = node.right
            
            # Find the leftmost node in the right subtree (inorder successor)
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            
            # If successor is not the immediate right child of the node to be deleted
            if successor_parent != node:
                # Remove successor from its current position
                successor_parent.left = successor.right
                # Give successor the right child of the node to be deleted
                successor.right = node.right
            
            # Give successor the left child of the node to be deleted
            successor.left = node.left
            
            # Return the successor to replace the deleted node
            return successor
        
        return node

    # Possible searches
    #   1. Empty Tree
    #   2. Not found nodes
    #   3. Found nodes
    def search(self, value):
        if not self.root:
            print("Empty tree")
            return
        
        cur_node = self.root

        while(cur_node):
            if value < cur_node.value:
                cur_node = cur_node.left
            elif value > cur_node.value:
                cur_node = cur_node.right
            else:
                print("Found!")
                return cur_node
        print("Not found!")
    
    def inorder_traversal(self):
        arr = []
        return self.inorder_recursive(self.root, arr)
    
    def inorder_recursive(self, node, arr):
        if node:
            self.inorder_recursive(node.left, arr)
            arr.append(node.value)
            self.inorder_recursive(node.right, arr)

        return arr

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
    new_bt.insert(1)
    new_bt.insert(5.5)
    visualize_tree.plot_hierarchical_tree(new_bt.root)

    new_bt.delete(5)
    visualize_tree.plot_hierarchical_tree(new_bt.root)

    print(new_bt.search(8))
    print(new_bt.search(10))
    print(new_bt.inorder_traversal())


def delete_test():
    pass

insert_test()