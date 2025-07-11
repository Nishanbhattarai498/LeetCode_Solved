# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both are None
        if not p and not q:
            return True
        # One of them is None or values don't match
        if not p or not q or p.val != q.val:
            return False
        # Recursively compare left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
