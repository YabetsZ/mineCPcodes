# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def insert(node, val):
            print("Here")
            if not(node.right or node.left):
                if node.val < val:
                    node.right = TreeNode(val)
                else:
                    node.left = TreeNode(val)
                return

            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)
            elif node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insert(node.right, val)
        
        mid = (len(nums) - 1)//2
        root = TreeNode(nums[mid])
        left = mid - 1
        for right in range(mid+1, len(nums)):
            insert(root, nums[right])
            if left >= 0:
                insert(root, nums[left])
            left -= 1
        return root

            