class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit integer limits
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        
        # Store the sign and work with the absolute value
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        reversed_x = 0
        
        # Pop digits from the end and push them to reversed_x
        while x != 0:
            digit = x % 10
            x //= 10
            reversed_x = (reversed_x * 10) + digit
            
        # Reapply the sign
        reversed_x *= sign
        
        # Check for 32-bit overflow
        if reversed_x < MIN_INT or reversed_x > MAX_INT:
            return 0
            
        return reversed_x