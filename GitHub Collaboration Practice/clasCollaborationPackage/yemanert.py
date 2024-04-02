# yemanert.py

class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to map Roman numerals to their integer values
        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the result
        result = 0
        
        # Iterate through the string from left to right
        for i in range(len(s)):
            # If the current numeral is smaller than the next numeral, subtract its value
            if i < len(s) - 1 and roman_to_int_map[s[i]] < roman_to_int_map[s[i + 1]]:
                result -= roman_to_int_map[s[i]]
            else:
                result += roman_to_int_map[s[i]]
        
        return result

# Example usage
roman_numeral = "MCMXCIV"
integer_value = Solution().romanToInt(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}")


