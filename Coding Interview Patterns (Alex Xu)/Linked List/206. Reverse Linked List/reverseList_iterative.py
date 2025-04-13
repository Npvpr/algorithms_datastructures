# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # think operation: 1 -> 2 -> 3 -> 4 -> 5
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node

            # for next step
            curr_node = next_node

        return prev_node