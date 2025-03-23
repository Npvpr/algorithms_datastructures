# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # checking root.left and root.right is not mandatory, it's just for optimization
        if not root or (not root.left and root.right):
            return root

        # swap first, traverse second -> order doesn't matter
        # traverse first, swap second -> will also be true
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root