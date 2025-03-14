# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(leftNode, rightNode):
            if bool(leftNode) ^ bool(rightNode):
                return False
            elif not leftNode and not rightNode:
                return True
            elif leftNode.val != rightNode.val:
                return False
            return check(leftNode.left, rightNode.right) and check(leftNode.right, rightNode.left)

        return check(root.left, root.right)