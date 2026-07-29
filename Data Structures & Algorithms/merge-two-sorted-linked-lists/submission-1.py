# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # List1 and List2
        # sorted

        # Approach
        # Invariant: Either one of the node from two list points first to main list
        # State    : left, right
        # Violation: When left == right, when one list links completely other one left out
        # Recover  : left <= right; left, left > right; right, 
        #            iteratively link the remaining left out nodes.
        # time: O(m+n), space=O(1) [left, right]

        def link(head, list3, node):
            if not head:
                head = node
                list3 = head
            else:
                list3.next = node
                list3 = list3.next
            
            return head, list3


        left, right = list1, list2
        list3 = None
        head = None

        while left and right:
            if left.val <= right.val:
                node = left
                left = left.next
            else:
                node = right
                right = right.next
            
            head, list3 = link(head, list3, node)

        while left:
            head, list3 = link(head, list3, left)
            left = left.next
        
        while right:
            head, list3 = link(head, list3, right)
            right = right.next

        return head
