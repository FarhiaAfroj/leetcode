class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
        decreasing = all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))

        return increasing or decreasing