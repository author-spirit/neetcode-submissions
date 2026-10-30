# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Invariant: if the p & q stays on two separate sub-tree then current node is LCA
        # state: current node
        # termination: if p & q splits then return current node
        if not root:
            return None

        val = root.val
        p_val = p.val
        q_val = q.val

        if val > p_val and val > q_val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if val < p_val and val < q_val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
        