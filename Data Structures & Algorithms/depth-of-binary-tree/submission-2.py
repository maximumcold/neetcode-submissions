# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0

        if not root:
            return count

        count += 1

        if not root.left and not root.right:
            return count

        else:
            count += max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        return count
