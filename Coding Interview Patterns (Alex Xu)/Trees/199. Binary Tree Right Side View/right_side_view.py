# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Main trick: Process previous queue and current queue at the same time
# Put all numbers of each level into a queue
# Replace the queue with numbers from the next level

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        # put root
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # if current i is last node of previous queue, append node(last node of current queue)
                if i == level_size - 1:
                    result.append(node.val)
        return result
