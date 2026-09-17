class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        product = 1
        total = 0

        for d in digits:
            product *= d
            total += d

        return product - total