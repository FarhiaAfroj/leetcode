from typing import Optional

# Definition for a binary tree node (LeetCode style).
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Helper to compute the depth of the leftmost path
        def depth(node: Optional[TreeNode]) -> int:
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        if not root:
            return 0

        left_depth = depth(root.left)
        right_depth = depth(root.right)

        if left_depth == right_depth:
            # Left subtree is perfect => 2^left_depth nodes there
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right subtree is perfect of height right_depth
            return (1 << right_depth) + self.countNodes(root.left)
