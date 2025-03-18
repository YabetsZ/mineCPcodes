# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, maxim, minim):
            if not node:
                return maxim - minim
            
            maxim = max(maxim, node.val)
            minim = min(minim, node.val)

            return max(dfs(node.right, maxim, minim), dfs(node.left, maxim, minim))
        
        return dfs(root, 0, float("inf"))