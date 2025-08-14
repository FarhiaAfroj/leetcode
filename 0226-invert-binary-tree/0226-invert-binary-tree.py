from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left  # Swap the children
            self.invertTree(root.left)  # Recursively invert the left subtree
            self.invertTree(root.right)  # Recursively invert the right subtree
        return root
