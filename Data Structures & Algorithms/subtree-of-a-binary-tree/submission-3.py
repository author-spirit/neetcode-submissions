# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Invariant: The node and its descendents are identical, 
        # if only it's structure and values are same
        # state: dfs and compare the subroot value
        # violate: if the structure is not identical
        # recover: return false

        if not root:
            return False

        def dfs(node, snode):
            if not node and not snode:
                return True

            if not node or not snode:
                return False

            if node.val != snode.val:
                return False
            
            left = dfs(node.left, snode.left)
            right = dfs(node.right, snode.right)
            if not left or not right:
                return False

            return True

        from collections import deque
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if dfs(node, subRoot):
                    return True
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return False
            


