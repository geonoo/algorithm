# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value == None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.left = make_tree_by(lst, 2 * idx + 2)

    return parent

longest = 0
root = make_tree_by([1,2,3,4,5],0)
def diameterOfBinaryTree(root: TreeNode) -> int:
    def dfs(node:TreeNode):
        global longest
        if not node:
            return -1

        left = dfs(node.left)
        right = dfs(node.right)

        longest = max(longest, left+right+2)
        return max(right,left)+1
    dfs(root)
    return longest
print(diameterOfBinaryTree(root))
