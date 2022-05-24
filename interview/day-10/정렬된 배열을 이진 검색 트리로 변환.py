from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST( nums:[int]) -> [TreeNode]:
    if not nums:
        return None

    mid = len(nums) // 2

    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid+1:])

    return node

def tree_to_list(root, l):

    if not root:
        return []
    lst = []
    q = deque()
    q.append(root)
    while q:
        if len(lst) > l:
            break
        node = q.popleft()
        if node:
            lst.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            lst.append(None)
    return lst


ll = [-10,-3,0,5,9]
r = sortedArrayToBST(ll)
print(tree_to_list(r, len(ll)))
