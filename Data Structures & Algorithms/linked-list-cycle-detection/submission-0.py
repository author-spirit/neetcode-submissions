# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # naive approach

        visited = set()
        visited.add(head)
        node = head

        while node:
            if node.next in visited:
                return True
            
            visited.add(node)
            node = node.next

        return False
        