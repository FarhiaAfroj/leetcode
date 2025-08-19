class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        sequence = [0, 1]
        for i in range(2, n+1):
            highest = 1 << (i-1)
            new_seq = [highest + num for num in reversed(sequence)]
            sequence += new_seq
        return sequence