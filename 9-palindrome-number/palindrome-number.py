class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) are never palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_half = 0
        
        # Reverse the second half of the number until it's greater than or equal to the first half
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            
        # For even-length numbers, x == reversed_half
        # For odd-length numbers, x == reversed_half // 10 (we discard the middle digit)
        return x == reversed_half or x == reversed_half // 10