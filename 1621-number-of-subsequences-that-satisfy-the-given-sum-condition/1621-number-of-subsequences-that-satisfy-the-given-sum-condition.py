class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1
        result = 0
        
        while left <= right:
            if nums[left] + nums[right] <= target:
    
                result = (result + pow(2, right - left, MOD)) % MOD
                left += 1
            else:
                right -= 1
        
        return result