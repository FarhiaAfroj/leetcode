class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            for j in range(min(len(w1), len(w2))):
                if rank[w1[j]] < rank[w2[j]]:
                    break
                if rank[w1[j]] > rank[w2[j]]:
                    return False
            else:
                if len(w1) > len(w2):
                    return False

        return True