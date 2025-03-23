# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this method cost 0(n^2) time complexity
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        queue = deque([root])

        while queue:
            cur_node = queue.popleft()

            if cur_node and (cur_node.left or cur_node.right):
                diff = abs(maxHeight(cur_node.left) - maxHeight(cur_node.right))
                # print(maxHeight(root.left), maxHeight(root.right))

                if diff > 1:
                    return False
                    
                queue.append(cur_node.left)
                queue.append(cur_node.right)

        return True

def maxHeight(root):

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        return max(maxHeight(root.left), maxHeight(root.right)) + 1