class Solution:
    def subarrayBitwiseORs(self, arr):
        ans = set()
        cur_or = set()
        for x in arr:
            nxt = {x}
            for v in cur_or:
                nxt.add(v | x)
            cur_or = nxt
            ans |= cur_or
        return len(ans)
