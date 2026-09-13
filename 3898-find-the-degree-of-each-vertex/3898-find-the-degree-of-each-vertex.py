class Solution:
    def findDegrees(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        for row in matrix:
            ans.append(sum(row))

        return ans