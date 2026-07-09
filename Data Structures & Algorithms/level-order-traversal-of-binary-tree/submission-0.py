# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        order = []
        q = deque([root])

        while(q):
            level_size = len(q)
            currentLevel = []

            for _ in range(level_size):
                current = q.popleft()
                currentLevel.append(current.val)

                q.append(current.left) if current.left else 0
                q.append(current.right) if current.right else 0
            
            order.append(currentLevel)

        return order
        