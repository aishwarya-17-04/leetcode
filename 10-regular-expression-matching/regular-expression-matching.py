class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if s[0...i-1] matches p[0...j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns that can match an empty string (e.g., "a*", "a*b*")
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the current characters match, or the pattern has a '.'
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # If the pattern has a '*'
                elif p[j - 1] == '*':
                    # Two cases for '*':
                    # 1. Zero occurrences of the preceding character (skip it and the '*')
                    dp[i][j] = dp[i][j - 2]
                    
                    # 2. One or more occurrences of the preceding character
                    # This is valid only if the preceding character in pattern matches the current character in string
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]