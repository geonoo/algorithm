# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: [TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

    def rangeSumBST2(self, root: [TreeNode], low: int, high: int) -> int:
        stack, sums = [root], 0

        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sums += node.val

        return sums

    def rangeSumBST3(self, root: [TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        return (root.val if low <= root.val <= high else 0) + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(
            root.right, low, high)

