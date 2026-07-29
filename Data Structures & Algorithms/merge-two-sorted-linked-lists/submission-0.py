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

        def link(head, list3, val):
            if not head:
                head = ListNode(val)
                list3 = head
            else:
                list3.next = ListNode(val)
                list3 = list3.next
            
            return head, list3


        left, right = list1, list2
        list3 = None
        head = None

        while left and right:
            if left.val <= right.val:
                val = left.val
                print("L", val)
                left = left.next
            else:
                val = right.val
                print("R", val)
                right = right.next
            
            head, list3 = link(head, list3, val)

        while left:
            head, list3 = link(head, list3, left.val)
            left = left.next
        

        
        while right:
            head, list3 = link(head, list3, right.val)
            right = right.next

        return head
