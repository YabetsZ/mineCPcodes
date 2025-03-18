# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findSuccessor(node):
            while node.left:
                node = node.left
            return node
        def delete(node, key):
            if not node:
                return None
            if node.val < key:
                node.right = delete(node.right, key)
            elif node.val > key:
                node.left = delete(node.left, key)
            else:
                if not(node.right or node.left):
                    return None
                elif bool(node.right) ^ bool(node.left):
                    return node.right if node.right else node.left
                else:
                    successor = findSuccessor(node.right)
                    node.val = successor.val
                    node.right = delete(node.right, node.val)
            return node
        
        return delete(root, key)

        