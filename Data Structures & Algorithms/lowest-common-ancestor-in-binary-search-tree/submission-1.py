# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        val = root.val
        p_val = p.val
        q_val = q.val

        if val > p_val and val > q_val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if val < p_val and val < q_val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if (val >= p_val and val <= q_val) or (val <= p_val and val >= q_val):
            return root
        