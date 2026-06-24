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
                return count, True

            right = depthSearch(root.right)
            left = depthSearch(root.left)
            
            if not right[1] or not left[1]:
                return count, False
            count += 1 
            print("Right: ", right)
            print("Left: ", left)
            print("ABS: ", right[0], left[0])
            print("+++++++++")

            if abs(right[0] - left[0]) > 1:
                print("ACK")
                return count, False
            
            if not root.left and not root.right:
                return count, True

            else:
                count += max(right[0], left[0])
        
            return count, True


        # if not root:
        #     return True

        # left = depthSearch(root.left)
        # right = depthSearch(root.right)

        # print("Right: ", right)
        # print("Left: ", left)
        
        # if not left[1] or not right[1]:
        #     return False

        # # if abs(left - right) > 1 or abs(right - left) > 1:
        # #     return False
        
        return depthSearch(root)[1]

