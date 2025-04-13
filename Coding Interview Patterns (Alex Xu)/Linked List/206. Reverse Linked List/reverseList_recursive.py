# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # recursive is basically dfs
    # goes to the last node first before doing any operation
    # think operation: 1 <- 2 <- 3 <- 4 <- 5
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # for empty node edge case and last node case
        if not head or not head.next:
            return head
        
        # this result is to carry last node to first call stack
        # call dfs here so the program goes to the last node first before doing any reversing
        result = self.reverseList(head.next)

        # reverse part
        head.next.next = head
        head.next = None

        return result