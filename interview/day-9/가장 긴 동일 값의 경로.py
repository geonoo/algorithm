# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return None
        parent = TreeNode(value)
        parent.left = make_tree(lst, idx*2+1)
        parent.right = make_tree(lst, idx*2+2)
    return parent

def longestUnivaluePath(root) -> int:
    rtn = [0]
    def dfs(node:TreeNode):
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)

        if node.left and node.val == node.left.val:
            left += 1
        else:
            left = 0

        if node.right and node.val == node.right.val:
            right += 1
        else:
            right = 0

        rtn.append(left+right)
        return max(left,right)

    dfs(root)
    return max(rtn)

r = make_tree([5,4,5,1,1,5],0)
print(longestUnivaluePath(r))