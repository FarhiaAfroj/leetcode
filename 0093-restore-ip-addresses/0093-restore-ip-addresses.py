class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            for end in range(start, min(start + 3, len(s))):
                part = s[start:end + 1]

                if len(part) > 1 and part[0] == '0':
                    break

                if int(part) > 255:
                    break

                parts.append(part)
                backtrack(end + 1, parts)
                parts.pop()

        backtrack(0, [])

        return result