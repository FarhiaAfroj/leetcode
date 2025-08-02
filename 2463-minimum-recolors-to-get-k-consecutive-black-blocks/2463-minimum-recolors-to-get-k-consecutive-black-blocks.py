class Solution:
    def minimumRecolors(self, blocks, k):
        cnt = blocks[:k].count('W')
        ans = cnt
        for i in range(k, len(blocks)):
            if blocks[i] == 'W': cnt += 1
            if blocks[i - k] == 'W': cnt -= 1
            ans = min(ans, cnt)
        return ans
