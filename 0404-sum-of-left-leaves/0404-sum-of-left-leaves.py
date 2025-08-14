class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        ans = 0
        # Check if left child exists and is a leaf
        if root.left and not root.left.left and not root.left.right:
            ans += root.left.val
        else:
            # Otherwise, recurse into left subtree
            ans += self.sumOfLeftLeaves(root.left)

        # Always recurse into right subtree
        ans += self.sumOfLeftLeaves(root.right)

        return ans
