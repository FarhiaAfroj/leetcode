class Solution:
    def sortedArrayToBST(self, nums):
        return self._build(nums, 0, len(nums) - 1)

    def _build(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self._build(nums, left, mid - 1)
        node.right = self._build(nums, mid + 1, right)
        return node
