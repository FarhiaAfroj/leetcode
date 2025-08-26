class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        from collections import defaultdict
        dp = defaultdict(set)
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                for jump in [k-1, k, k+1]:
                    if jump > 0 and stone + jump in stone_set:
                        dp[stone + jump].add(jump)
        return len(dp[stones[-1]]) > 0