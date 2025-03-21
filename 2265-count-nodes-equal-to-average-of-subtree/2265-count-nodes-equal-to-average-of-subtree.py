# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode, count = 0) -> int:
        def calculate(node, count):
            if not node:
                return (0, 0, 0)

            leftSum, leftNodes, countLeft = calculate(node.left, count)
            rightSum, rightNodes, countRight = calculate(node.right, count)
            wholeSum = leftSum + rightSum + node.val
            nodesCount = leftNodes + rightNodes+ 1
            if wholeSum//(nodesCount) == node.val:
                count += 1
            count += countLeft + countRight

            return (wholeSum, nodesCount, count)
        wholeSum, nodesCount, count = calculate(root, 0)
        return count