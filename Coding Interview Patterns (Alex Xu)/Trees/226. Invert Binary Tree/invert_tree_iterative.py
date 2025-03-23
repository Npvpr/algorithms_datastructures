# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = deque([root])

        while queue:
            cur_node = queue.popleft()
            if cur_node and (cur_node.left or cur_node.right):
                cur_node.left, cur_node.right = cur_node.right, cur_node.left
                queue.append(cur_node.left)
                queue.append(cur_node.right)
        
        return root