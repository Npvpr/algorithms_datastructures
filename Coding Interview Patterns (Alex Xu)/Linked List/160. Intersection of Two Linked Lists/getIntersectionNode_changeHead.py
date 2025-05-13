# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Total length method
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        left, right = headA, headB
        
        while left != right:
            left = left.next if left else headB
            right = right.next if right else headA

        return left