# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []

        def leftdfs(node):
            if not node:
                return left.append(None)
            left.append(node.val)
            leftdfs(node.left)
            leftdfs(node.right)
        def rightdfs(node):
            if not node:
                return right.append(None)
            right.append(node.val)
            rightdfs(node.right)
            rightdfs(node.left)
        leftdfs(root.left)
        rightdfs(root.right)
        return right == left