# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Invariant: The recursion only returns the maximum subtree value
        # state: maximum path sum
        # termination: no longer split

        if not root:
            return 0

        self.maxsum = root.val

        def max_path(node):
            if not node:
                return 0
            
            left = max_path(node.left)
            right = max_path(node.right)

            # To avoid -ve
            left = max(left, 0)
            right = max(right, 0)

            self.maxsum = max(self.maxsum, left + right + node.val)
            return node.val + max(left, right)
        
        val = max_path(root)
        print(val)
        return max(self.maxsum, val)
        