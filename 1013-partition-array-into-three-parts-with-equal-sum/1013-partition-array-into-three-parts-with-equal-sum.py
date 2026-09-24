class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        count = 0
        current = 0

        for i in range(len(arr) - 1):
            current += arr[i]

            if current == target:
                count += 1
                current = 0

                if count == 2:
                    return True

        return False