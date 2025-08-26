class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        F0 = 0
        for i in range(n):
            F0 += i * nums[i]
        
        max_val = F0
        current = F0
        for k in range(1, n):
            current = current + total_sum - n * nums[n - k]
            if current > max_val:
                max_val = current
        
        return max_val