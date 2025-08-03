import bisect  # built-in module

class Solution:
    def maximumCount(self, nums):
        neg = bisect.bisect_left(nums, 0)
        pos = len(nums) - bisect.bisect_right(nums, 0)
        return pos if pos > neg else neg
        