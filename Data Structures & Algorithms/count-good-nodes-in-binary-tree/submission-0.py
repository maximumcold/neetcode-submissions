# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def countGood(root, greatest_so_far) -> int:
            
            count = 0

            if not root:
                return 0
            
            if root.val >= greatest_so_far:
                count += 1
                greatest_so_far = root.val

            if root.left:
                count += countGood(root.left, greatest_so_far)


            if root.right:
                count += countGood(root.right, greatest_so_far)

            

            return count
            

        output = 0

        if not root:
            return output

        output += countGood(root, root.val)
        print(output)

        return output
        
