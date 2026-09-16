class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x % 2 == 0]
        odd = [x for x in nums if x % 2 == 1]

        result = []

        for i in range(len(even)):
            result.append(even[i])
            result.append(odd[i])

        return result