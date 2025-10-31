class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        
        dp = [0] * (2 * total + 1)
        dp[total] = 1
        
        for num in nums:
            next_dp = [0] * (2 * total + 1)
            for s in range(2 * total + 1):
                if dp[s] != 0:
                    next_dp[s + num] += dp[s]
                    next_dp[s - num] += dp[s]
            dp = next_dp
        
        return dp[total + target]