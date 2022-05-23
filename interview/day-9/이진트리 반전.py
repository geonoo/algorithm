# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is not None:
            parent = TreeNode(value)
            parent.left = list_to_tree(lst, idx*2+1)
            parent.right = list_to_tree(lst, idx*2+2)
    return parent

def tree_len(root):
    cnt = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node is not None:
            cnt += 1
            stack.append(node.left)
            stack.append(node.right)
    return cnt

def tree_to_list(root, lst, idx=0):
    node = root
    if node:
        lst[idx] = node.val
    if node.left:
        tree_to_list(node.left, lst, idx * 2 + 1)
    if node.right:
        tree_to_list(node.right, lst, idx * 2 + 2)

    return lst

def invertTree(root: [TreeNode]) -> [TreeNode]:
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)
    return root

r = list_to_tree([4,2,7,1,3,6,9], 0)
lst = tree_to_list(r,[0]*tree_len(r))
print(lst)
invertR = invertTree(r)
print(tree_to_list(invertR,[0]*tree_len(invertR)))