# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Invariant: Inorder traversal in BST follows strictly increasking order
        #            if count == k then kth smallest
        # state: count, result
        # terminate: when count == k, return kth smallest 
        # pattern: BST + inorder

        self.count = 0
        self.res = 0

        def inorder(node):
            if not node:
                return
        
            inorder(node.left)
            if self.count == k:
                return

            self.count +=1
            self.res = node.val
            inorder(node.right)
        
        inorder(root)
        return self.res
