# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Reorder -> [0,n-1, 1, n-2, 2, n-3, 3, ...]

        # [0, 1, 2, 3, 4, 5, 6]
        # [0, 6, 1, 5, 2, 4, 3]
        
        # Naive approach
        # Every every odd position the reorder
        # state: current, get n-x, prev, N

        # Better approach
        # Invariant: Before the i nodes are already reordered.
        # State: Every 2 step update i.e slow-fast pointer
        # Violation: Any reordered node next will be null
        # Recover: Point the left node to reorder node.next

        slow = head
        fast = head
        second = None

        # 1. Split into half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
            
        # 2. reverse second half
        # 4,5,6, 7
        # prev=None, 4.next = None
        # prev=4, 5.next = 4
        # prev=5, 6.next = 5
        
        cur = second
        prev = None
        while cur:
            print("Rev", prev and prev.val, cur.val)
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        # previous holds the half
        second = prev

        # 3. Merge
        node = head
        prev = None
        while second:
            next = node.next
            node.next = second
            second = second.next
            node.next.next = next
            
            node = next





