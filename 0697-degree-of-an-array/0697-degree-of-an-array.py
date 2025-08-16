from collections import Counter
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = Counter(nums)
        degree = max(counts.values())
        
        left, right = {}, {}
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
        
        min_length = len(nums)
        for num, freq in counts.items():
            if freq == degree:
                current_length = right[num] - left[num] + 1
                min_length = min(min_length, current_length)
        
        return min_length
