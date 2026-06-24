# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depthSearch(root) -> int:
            count = 0
            if not root:
                return count

            count += 1

            if not root.left and not root.right:
                return count

            else:
                count += max(depthSearch(root.left), depthSearch(root.right))
            
            nonlocal longest_path
            longest_path = max(longest_path, (depthSearch(root.left) + depthSearch(root.right)))
            
            return count


        longest_path = 0
        total_path = 0


        r_path = depthSearch(root.right)

        l_path = depthSearch(root.left)

        if not root:
            return 0

        # print("Total path: ", total_path)

        depthSearch(root)

        if total_path >= longest_path:
            longest_path = total_path

        
        return longest_path
        
        
        