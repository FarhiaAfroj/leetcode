class Solution(object):
    def countAndSay(self, n):
        # Base case
        result = "1"
        # Generate from 2 to n
        for _ in range(1, n):
            current = ""
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1
                current += str(count) + result[i]
                i += 1
            result = current
        return result
