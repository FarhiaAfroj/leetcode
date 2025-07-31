class Solution:
    def longestSubarray(self, nums):
        # Find the maximum value in nums
        max_val = max(nums)
        max_len = 0
        curr = 0
        
        # Traverse array
        for x in nums:
            if x == max_val:
                curr += 1
                if curr > max_len:
                    max_len = curr
            else:
                curr = 0
        
        return max_len

