# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Solution Article: https://vishwanathts.hashnode.dev/maximum-depth-of-a-binary-tree-leetcode-solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if root:
            print(f"Visiting Node with value: {root.val}")
        else:
            print("Visiting None node")
        
        if not root:
            return 0

        # Debug: Recursive call to left subtree
        left_depth = self.maxDepth(root.left)
        print(f"Left depth of node {root.val if root else 'None'}: {left_depth}")

        # Debug: Recursive call to right subtree
        right_depth = self.maxDepth(root.right)
        print(f"Right depth of node {root.val if root else 'None'}: {right_depth}")

        # Debug: Calculate max depth
        current_depth = 1 + max(left_depth, right_depth)
        print(f"Max depth at node {root.val if root else 'None'}: {current_depth}")

        return current_depth

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(f"Maximum Depth of the Binary Tree: {sol.maxDepth(root)}")

