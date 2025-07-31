class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case explicitly
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        
        # Subtract divisor multiplied by powers of two from dividend
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            
            # Increase temp_divisor exponentially by shifting left
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            dividend -= temp_divisor
            quotient += multiple
        
        return sign * quotient
