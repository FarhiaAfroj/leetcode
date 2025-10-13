class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        for i, num in enumerate(nums):
            if i != max_index and max_val < 2 * num:
                return -1
        
        return max_index
        