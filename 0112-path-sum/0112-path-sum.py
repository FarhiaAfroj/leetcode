class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))
