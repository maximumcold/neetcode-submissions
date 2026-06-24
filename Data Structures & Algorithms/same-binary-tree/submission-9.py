# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        right = True
        left = True

        if not p and q:
            return False

        if not q and p:
            return False

        if not q and not p:
            return True

        if p.val == q.val:
        
            left = self.isSameTree(p.left, q.left)

            right = self.isSameTree(p.right, q.right)

            return left and right

        else:
            return False

        return right and left
        