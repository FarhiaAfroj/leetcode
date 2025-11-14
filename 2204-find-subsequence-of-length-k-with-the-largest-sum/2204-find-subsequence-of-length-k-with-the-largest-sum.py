class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
       
        indexed = sorted([(num, i) for i, num in enumerate(nums)], key=lambda x: -x[0])
       
        result = sorted(indexed[:k], key=lambda x: x[1])
        return [num for num, idx in result]