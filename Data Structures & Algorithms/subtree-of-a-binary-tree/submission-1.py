# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
                
            if not q and not p:
                return True

            if  not p and q or not q and p or p.val != q.val:
                return False
            
            left = isSameTree(p.left, q.left)

            right =isSameTree(p.right, q.right)

            return left and right

        if not root and not subRoot:
            return True
        
        if root and subRoot:
            print("ACK")

            if root.val == subRoot.val:

                if not isSameTree(root, subRoot):
                    left = self.isSubtree(root.left, subRoot)
                    right = self.isSubtree(root.right, subRoot)
                    print("Left: ", left)
                    print("Right: ", right)
                    return left or right
                else:
                    return True
            
            else:
                left = self.isSubtree(root.left, subRoot)
                right = self.isSubtree(root.right, subRoot)
                return left or right
        return False
            
