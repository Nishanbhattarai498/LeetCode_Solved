# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0
        def dfs(node):
            if not node:
                return 0  # Height is 0 if node is None

            # Recursively get the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update diameter at this node (sum of left and right heights)
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return height of this subtree
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.max_diameter