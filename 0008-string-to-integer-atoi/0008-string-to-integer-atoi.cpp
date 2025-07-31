#include <string>
#include <climits>

class Solution {
public:
    int myAtoi(const std::string& s) {
        int i = 0, n = s.size();
        // 1) Skip leading whitespace
        while (i < n && s[i] == ' ') i++;
        if (i >= n) return 0;

        // 2) Handle optional sign
        int sign = 1;
        if (s[i] == '+' || s[i] == '-') {
            if (s[i] == '-') sign = -1;
            i++;
        }

        // 3) Parse digits and build the number
        long result = 0;
        while (i < n && std::isdigit(s[i])) {
            int digit = s[i] - '0';

            // 4) Check for overflow before incorporating digit
            if (result > INT_MAX / 10 ||
                (result == INT_MAX / 10 && digit > INT_MAX % 10)) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }

            result = result * 10 + digit;
            i++;
        }

        return static_cast<int>(sign * result);
    }
};
