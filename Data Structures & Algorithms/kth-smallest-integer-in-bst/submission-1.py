# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        sortedArr = []
        self.counter = 0

        def inOrder(node):
            if not node or self.counter == k :
                return

            inOrder(node.left)

            sortedArr.append(node)
            self.counter += 1 

            inOrder(node.right)

        inOrder(root)

        return sortedArr[k-1].val