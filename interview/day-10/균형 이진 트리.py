# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        maxDiff = 0

        def dfs(node: TreeNode):
            nonlocal maxDiff
            if not node:
                return 0
            if not (node.left or node.right):
                return 1

            leftDepth = dfs(node.left) + 1
            rightDepth = dfs(node.right) + 1

            maxDiff = max(maxDiff, abs(leftDepth - rightDepth))
            return max(leftDepth, rightDepth)

        dfs(root)
        return maxDiff <= 1