# Link: https://leetcode.com/problems/same-tree/description/
# Solution Article: https://vishwanathts.hashnode.dev/comparing-two-binary-trees-for-equality-leetcode-solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.iSameTree(p.left, q.left) and 
                self.iSameTree(p.right, q.right))
        