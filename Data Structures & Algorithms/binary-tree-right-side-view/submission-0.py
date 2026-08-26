# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Invariant: The last node of each level are considered right side view
        # State: BFS, remember: qSize, result
        # Violate: If end of level
        # Recover: Store it in list, recalculate qSize

        if not root:
            return []
        
        from collections import deque
        queue = deque([root])
        qSize = len(queue)
        result = []

        while queue:
            node = None
            for _ in range(qSize):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            qSize = len(queue)
            result.append(node.val)
        return result


