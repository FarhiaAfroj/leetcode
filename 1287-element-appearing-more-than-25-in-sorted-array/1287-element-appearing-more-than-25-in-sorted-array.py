class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                count = 1

            if count * 4 > len(arr):
                return arr[i]

        return arr[0]