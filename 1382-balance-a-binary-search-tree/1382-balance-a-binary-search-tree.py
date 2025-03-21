# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def collect(node):
            if not node:
                return
            collect(node.left)
            elems.append(node.val)
            collect(node.right)
        def construct(arr):
            if len(arr) == 0:
                return None
            mid = len(arr)//2
            left = construct(arr[:mid])
            right = construct(arr[mid+1:])
            return TreeNode(arr[mid], left, right)
        elems = []
        collect(root)
        
        return construct(elems)
