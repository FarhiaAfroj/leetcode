class Solution:
    def multiply(self, num1, num2):
        # Step 1: handle zero case
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        # result array for digits
        res = [0] * (m + n)

        # Step 2: multiply digits bottom-up
        for i in range(m - 1, -1, -1):
            a = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                b = ord(num2[j]) - ord('0')
                mul = a * b
                sum_val = mul + res[i + j + 1]
                res[i + j + 1] = sum_val % 10
                res[i + j] += sum_val // 10

        # Step 3: convert to string, skipping leading zeros
        index = 0
        while index < len(res) and res[index] == 0:
            index += 1

        result_str = ''.join(str(d) for d in res[index:])
        return result_str if result_str else "0"

        