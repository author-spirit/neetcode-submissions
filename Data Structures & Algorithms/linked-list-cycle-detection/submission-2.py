# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Better approach
        # Slow-fast pointer

        # Invariant: Any one node meet up at one time
        # State: slow-fast node
        # Violation: If none of them meet
        # Restore: return false if no cycle

        slow = head         #1
        fast = None

        if head and head.next:
            fast = head.next.next

        while fast and fast.next:
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next
        
        return False




        