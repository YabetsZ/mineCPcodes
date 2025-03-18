# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def dfs(node, level):
            if not node:
                return
            if len(result) -1 < level:
                result.append(deque())

            if level%2:
                result[level].appendleft(node.val)
            else:
                result[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            # else:
            #     dfs(node.left, level+1)
            #     dfs(node.right, level+1)
        dfs(root, 0)
        return [list(x) for x in result]