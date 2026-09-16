class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)

        diff = (alice_total - bob_total) // 2
        bob = set(bobSizes)

        for a in aliceSizes:
            b = a - diff
            if b in bob:
                return [a, b]