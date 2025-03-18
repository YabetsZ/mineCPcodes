# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not(root.right, root.left):
            return root
        def dfs(l_node, r_node,  level):
            if not(l_node or r_node):
                return
            if level%2:
                r_node.val, l_node.val = [l_node.val, r_node.val]
            
            dfs(l_node.left, r_node.right, level+1)
            dfs(l_node.right, r_node.left, level+1)
        dfs(root.left, root.right, 1)
        return root


