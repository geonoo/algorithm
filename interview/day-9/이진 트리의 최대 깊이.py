from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value == None:
            return

        parent = TreeNode(value)
        parent.left = make_tree(lst, 2*idx+1)
        parent.right = make_tree(lst, 2*idx+2)

    return parent

def maxDepth(lst) -> int:
    root = make_tree(lst, 0)
    if not root:
        return 0

    q = deque([root])
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth

print(maxDepth([3,9,20,None,None,15,7]))