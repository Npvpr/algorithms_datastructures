# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None

        def remove(current_node, n):

            if not current_node.next:
                return n

            n = remove(current_node.next, n) - 1

            if n == 0:
                current_node.next = current_node.next.next
           
            # print("Node: " + str(current_node.val))
            # print("Count: " + str(n))
            return n

        n = remove(head, n)

        if n == 1:
            return head.next
        
        return head
