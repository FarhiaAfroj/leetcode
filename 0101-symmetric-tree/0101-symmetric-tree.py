from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        q = deque([root.left, root.right])

        while q:
            p = q.popleft()
            q2 = q.popleft()
            if not p and not q2:
                continue
            if not p or not q2 or p.val != q2.val:
                return False
            q.append(p.left)
            q.append(q2.right)
            q.append(p.right)
            q.append(q2.left)

        return True

