class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque

        queue = deque([(root, None)])

        while queue:
            x_parent = None
            y_parent = None

            for _ in range(len(queue)):
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent

                if node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left, node))

                if node.right:
                    queue.append((node.right, node))

            if x_parent is not None or y_parent is not None:
                return x_parent is not None and y_parent is not None and x_parent != y_parent

        return False