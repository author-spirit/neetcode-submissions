# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST - Validation
        # Invariant: Left <= parent < right
        # State: Traversal - DFS, left and right checks
        # Violate: If left <= parent < right not matched
        # Recover: Return false

        if not root:
            return True

        def check_valid(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False
            
            left = check_valid(node.left, left, node.val)
            right = check_valid(node.right, node.val, right)
            return left and right

        return check_valid(root, -1000000000, 1000000000)
        