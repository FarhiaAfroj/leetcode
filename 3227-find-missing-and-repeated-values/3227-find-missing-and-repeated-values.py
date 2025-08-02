class Solution:
    def findMissingAndRepeatedValues(self, grid):
        """
        grid: list of lists of ints (rows of the n x n matrix)
        Return: [repeating_number, missing_number]
        """

        n = len(grid)
        N = n * n

        # Frequency array for 1..N
        freq = [0] * (N + 1)
        for row in grid:
            for x in row:
                freq[x] += 1

        repeating = missing = -1
        for num in range(1, N + 1):
            if freq[num] == 2:
                repeating = num
            elif freq[num] == 0:
                missing = num

        return [repeating, missing]


