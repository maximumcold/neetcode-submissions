# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        q = []
        level = 0

        q.append([root, level])

        if not root:
            return []

        build_levels = []
        output = []

        temp_list = []
        stored_depth = 0
        
        while q:
            c_node = q.pop(0)
            if not c_node:
                break
            node = c_node[0]
            depth = c_node[1]

            if stored_depth < depth:
                stored_depth = depth
                build_levels.append(temp_list)
                temp_list = []

            
            if c_node[0].left:
                q.append([node.left, depth + 1])

            if c_node[0].right:
                q.append([node.right, depth + 1])
        
            temp_list.append(node.val)
        
        build_levels.append(temp_list)
        
        
        for level in build_levels:
            output.append(level[-1])

        return output

