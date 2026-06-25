# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_branches(root):

            left_min = float('inf')
            left_max = -float('inf')

            right_min = float('inf')
            right_max = -float('inf')

            is_valid = True

            if root:
                curr_min = root.val
                curr_max = root.val
            else:
                return min(left_min, right_min), max(left_max, right_max), is_valid

            if root.left:
                left_min, left_max, valid = check_branches(root.left)

                if is_valid:
                    is_valid = valid
            
            if root.right:
                right_min, right_max, valid = check_branches(root.right)
                if is_valid:
                    is_valid = valid

            if not root.left and not root.right:
                return root.val, root.val, True

    
            if left_max >= curr_min:
                is_valid = False

            if right_min <= curr_max:
                is_valid = False

            return min(left_min, right_min, curr_min), max(left_max, right_max, curr_max), is_valid

        min_val, max_val, valid = check_branches(root)

        return valid
        