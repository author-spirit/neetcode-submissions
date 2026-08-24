# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        from collections import deque
        queue = deque([root])
        qSize = len(queue)

        result = []
        sublist = []
        while queue:
            node = queue.popleft()
            sublist.append(node.val)
            qSize -=1

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

            if qSize == 0:
                qSize = len(queue)
                result.append(sublist)
                sublist = []
        
        return result