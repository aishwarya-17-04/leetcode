class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Ignore leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        
        # 2. Determine the sign
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
            
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # 3. Convert characters to integer
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit
            index += 1
            
        # Apply the sign
        result *= sign
        
        # 4. Rounding / Clamping to 32-bit signed integer range
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
            
        return result