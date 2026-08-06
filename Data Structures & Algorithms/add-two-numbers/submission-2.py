class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Reversed Linked List
        # L1 = 3,2,1 (is equal size?)
        # L2 = 6,5,4
        # Out = 9,7,5 -> 5,7,9 (Reverse)

        # Brute-force
        # Combine two, if any left out just add to new LL
        # Unreverse the result LL

        if not l1 and not l2: return None
        if l1.val == 0 and not l1.next and l2.val == 0 and not l2.next: return ListNode(0)

        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            
            curr.next = ListNode(val)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next