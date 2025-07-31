class Solution:
    def reverse(self, x):
        INT_MAX =  2**31 - 1
        INT_MIN = -2**31

        ans = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            # Check for overflow before actually multiplying/adding
            if ans > INT_MAX // 10 or (ans == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            ans = ans * 10 + digit

        ans *= sign
        # Final boundary check (optional, since we checked per digit)
        if ans < INT_MIN or ans > INT_MAX:
            return 0
        return ans
