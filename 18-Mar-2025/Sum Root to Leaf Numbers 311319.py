# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, tot, num):
            num = num*10 + node.val
            if not(node.left or node.right):
                tot += num
            
            if node.left:
                tot = dfs(node.left, tot, num)
            if node.right:
                tot = dfs(node.right, tot, num)
            
            return tot
        return dfs(root, 0, 0)
            