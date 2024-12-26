# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Solution Article: https://vishwanathts.hashnode.dev/in-order-traversal-of-a-binary-tree-using-recursion-leetcode-solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)

        return result