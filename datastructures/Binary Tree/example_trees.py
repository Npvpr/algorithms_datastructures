import visualize_tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# No restrictions, as long as maximum children is 2 for each node
def binary_tree():

    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    bt = node1
    node1.left = node2
    node2.left = node3
    node2.right = node4
    node1.right = node5
    node5.left = node6
    node5.right = node7
    node6.left = node8
    node6.right = node9
    node9.right = node0

    visualize_tree.plot_hierarchical_tree(bt, "Binary Tree")

# All nodes on the left side must be smaller than the current/each node
# All nodes on the right side must be bigger than or equal to the current/each node
# Equal nodes are put to the right side of node
# When deleting, replace current node with either smallest from the right side or largest from the left side
def binary_search_tree():

    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    bst = node7
    node7.left = node6
    node6.left = node5
    node5.left = node4
    node4.left = node3
    node3.left = node2
    node2.left = node1
    node1.left = node0
    node7.right = node8
    node8.right = node9

    visualize_tree.plot_hierarchical_tree(bst, "Binary Search Tree")

# Create and visualize the trees
binary_tree()
#binary_search_tree()