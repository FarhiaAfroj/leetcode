class Solution:
    def binaryGap(self, n: int) -> int:
        positions = []

        for i, bit in enumerate(bin(n)[:1:-1]):
            if bit == "1":
                positions.append(i)

        if len(positions) < 2:
            return 0

        return max(positions[i] - positions[i - 1] for i in range(1, len(positions)))