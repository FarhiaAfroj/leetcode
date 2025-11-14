class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(n):
            for j in range(max(0, i - k), min(n, i + k + 1)):
                if nums[j] == key:
                    result.append(i)
                    break
        
        return result