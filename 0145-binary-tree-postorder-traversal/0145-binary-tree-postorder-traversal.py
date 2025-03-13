# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def traverse(root, arr):
            if root is None:
                return
            traverse(root.left, arr)
            traverse(root.right, arr)
            arr.append(root.val)
        traverse(root, arr)
        return arr