# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def checkSubtree(root, p, q) -> int:
            count = 0

            if not root:
                return count

            if count > 1:
                return count

            if root.val == p.val or root.val == q.val:
                count += 1
            
            count += checkSubtree(root.left, p, q) + checkSubtree(root.right, p, q)
            # print("Check: ", count)
            return count

        if not root:
            return False

        new_root = root

        check_left = checkSubtree(root.left, p, q)
        check_right = checkSubtree(root.right, p, q)
        print("Root: ", root.val, "Check: ")
        
        if check_left == 2:
            if root.val == p or root.val == q:
                return root

            if root.left:
                new_root = self.lowestCommonAncestor(root.left, p, q)

            elif root.right:
                new_root = self.lowestCommonAncestor(root.right, p, q)
            return new_root

        elif check_left == 1 or check_right == 1:
            return root
        
        elif check_left == 0:
            if root.right:
                new_root = self.lowestCommonAncestor(root.right, p, q)
            elif root.left:
                new_root = self.lowestCommonAncestor(root.right, p, q)
            return new_root

        return root


            

                
                
