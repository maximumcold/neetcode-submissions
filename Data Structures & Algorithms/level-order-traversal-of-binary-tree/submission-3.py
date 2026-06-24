# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        layer = 0
        q = []
        level = 0

        q.append([root, level])

        if not root:
            return []

        output = []

        temp_list = []
        stored_depth = 0
        
        while q:
            c_node = q.pop(0)
            
            node = c_node[0]
            depth = c_node[1]

            if stored_depth < depth:
                stored_depth = depth
                output.append(temp_list)
                temp_list = []

            
            if c_node[0].left:
                q.append([node.left, depth + 1])

            if c_node[0].right:
                q.append([node.right, depth + 1])
        
            temp_list.append(node.val)
        
        output.append(temp_list)
        
        return output
