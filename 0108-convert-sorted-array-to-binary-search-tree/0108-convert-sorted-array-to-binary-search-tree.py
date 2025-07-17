# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def insert(arr):
            # print("Here")
            if not arr:
                return None
            elif len(arr) == 1:
                return TreeNode(arr[0])
            
            mid = len(arr)//2
            node = TreeNode(arr[mid])
            node.left = insert(arr[:mid])
            node.right = insert(arr[mid+1:])
            return node
        return insert(nums)

            