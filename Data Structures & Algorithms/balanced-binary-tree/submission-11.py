# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depthSearch(root) -> int:
            count = 0
            if not root:
                return count

            right = depthSearch(root.right)
            left = depthSearch(root.left)
            
            if right == -1 or left == -1:
                return -1

            count += 1 
            if abs(right - left) > 1:
                return -1
            
            if not root.left and not root.right:
                return count
            else:
                count += max(right, left)
        
            return count
        
        return depthSearch(root) != -1

