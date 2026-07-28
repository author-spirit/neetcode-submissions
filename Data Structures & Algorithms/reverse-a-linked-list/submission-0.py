# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 0,1,2,3 -> 3,2,1,0
        # Naive approach
        # Put it in LIFO way

        # Better approach
        # Pattern: recursive follow - node
        # invariant: nodes are linearly linked
        # state: hold the each node in LIFO order
        # violation: when there is no node linked to next
        # recover: stop the execution when no next node to process.

        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        # node = 3
        # node.next -> 2
        # node.next.next -> 1
        # node.next.next.next -> 0
        
        while stack:
            head.next = ListNode(stack.pop(), None)
        
