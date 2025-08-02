import math

class Solution:
    def closestPrimes(self, left, right):
        # type: (int, int) -> list[int]
        sieve = [True] * (right + 1)
        if right >= 0:
            sieve[0] = False
        if right >= 1:
            sieve[1] = False

        limit = int(math.sqrt(right))
        for i in range(2, limit + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False

        primes = []
        for p in range(left, right + 1):
            if p >= 2 and sieve[p]:
                primes.append(p)

        if len(primes) < 2:
            return [-1, -1]

        best = [-1, -1]
        min_gap = float("inf")
        prev = primes[0]

        for curr in primes[1:]:
            gap = curr - prev
            if gap < min_gap:
                min_gap = gap
                best = [prev, curr]
                if gap == 1:
                    break
            prev = curr

        return best


        