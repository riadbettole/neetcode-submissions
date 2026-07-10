# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedArr = []

        def inOrder(node):
            if not node:
                return

            inOrder(node.left)

            sortedArr.append(node)
            
            inOrder(node.right)

        inOrder(root)

        return sortedArr[k-1].val