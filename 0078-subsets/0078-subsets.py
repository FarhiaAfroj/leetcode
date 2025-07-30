class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)

        def dfs(start, path):
            res.append(path[:])  # Capture the current subset
            for i in range(start, n):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res
