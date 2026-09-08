# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST - Validation
        # Invariant: Every node must satisfy the range (left, right) from the ancestors
        # State: 
        #       left_node = (left, parent)
        #       right_node = (parent, right)
        # Violate: if left < node < right not satisfied
        # Recover: Return false

        if not root:
            return True

        def check_valid(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False
            
            return check_valid(node.left, left, node.val) and check_valid(node.right, node.val, right)

        return check_valid(root, float("-Inf"), float("Inf"))
        