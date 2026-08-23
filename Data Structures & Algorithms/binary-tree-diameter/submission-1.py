# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Pattern: DFS (Treat Subtree root as breakpoint)
        # Invariant: Subtree makes up new diameter
        # Violates: Max edges between subtree and upward subtree
        # Recover: Take the max edge count

        self.maxDiameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            self.maxDiameter = max(self.maxDiameter, left + right)

            height = max(left, right)
            return height + 1
        
        dfs(root)
        return self.maxDiameter

        
