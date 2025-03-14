# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sum_it(node, reach):
            if node is None:
                if reach == targetSum:
                    return True
                else:
                    return False
            
            reach = node.val + reach if reach is not None else node.val
            
            return sum_it(node.left, reach) or sum_it(node.right, reach)
        return sum_it(root, None)
