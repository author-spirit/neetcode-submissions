# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Brute-force
        # store it in list and remove n-1

        nlist = []
        node = head

        while node:
            nlist.append(node)
            node = node.next
        
        pos = len(nlist) - n
        nth = nlist[pos]
        
        node = head
        prev = None

        while node:
            # Delink nth node
            if nth == node:
                if prev is None:
                    head = head.next
                else:
                    prev.next = node.next
                break

            prev = node
            node = node.next 

        return head
        