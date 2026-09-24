class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there's only 1 row or the string is shorter than the number of rows, 
        # no zigzagging is needed.
        if numRows == 1 or numRows >= len(s):
            return s
            
        # Create an array of strings to represent each row
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        # Iterate through the string and place characters in the correct row
        for char in s:
            rows[current_row] += char
            
            # Change direction when hitting the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move up or down
            current_row += 1 if going_down else -1
            
        # Combine all rows into a single string
        return "".join(rows)