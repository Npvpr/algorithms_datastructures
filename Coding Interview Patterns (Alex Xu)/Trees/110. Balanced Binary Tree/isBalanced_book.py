# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this method cost 0(n) time complexity
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool: # type: ignore

        return maxHeight_isBalanced(root) != -1

def maxHeight_isBalanced(node):

        if not node:
            return 0
        
        left_height = maxHeight_isBalanced(node.left)
        right_height = maxHeight_isBalanced(node.right)

        # at some point down the road, a subtree is unbalanced
        if left_height == -1 or right_height == -1:
            return -1
        
        diff = abs(left_height - right_height)
        # current subtree is unbalanced
        if diff > 1:
            return -1
        
        # current subtree is still balanced, so return current height of the subtree
        return 1 + max(left_height, right_height)
        