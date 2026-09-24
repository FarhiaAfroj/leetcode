class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return True

            if node.val != root.val:
                return False

            return dfs(node.left) and dfs(node.right)

        return dfs(root)