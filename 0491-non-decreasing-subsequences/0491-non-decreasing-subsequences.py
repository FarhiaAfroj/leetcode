class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n = len(nums)
        
        def backtrack(idx, sequence):
            if idx == n:
                if len(sequence) >= 2:
                    result.add(tuple(sequence))
                return
            
            if not sequence or nums[idx] >= sequence[-1]:
                backtrack(idx + 1, sequence + [nums[idx]])
            
            backtrack(idx + 1, sequence)
        
        backtrack(0, [])
        return list(result)