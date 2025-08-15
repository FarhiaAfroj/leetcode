
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode):
        from collections import defaultdict

        freq = defaultdict(int)

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            freq[node.val] += 1
            inorder(node.right)

        inorder(root)

        max_freq = max(freq.values())
        return [val for val, count in freq.items() if count == max_freq]
