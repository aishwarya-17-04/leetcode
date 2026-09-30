class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the values and their corresponding Roman numeral symbols, 
        # including the subtractive combinations, in descending order.
        value_symbol_pairs = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        
        for value, symbol in value_symbol_pairs:
            if num == 0:
                break
            
            # Find how many times the current value fits into num
            count, num = divmod(num, value)
            result.append(symbol * count)
            
        return "".join(result)