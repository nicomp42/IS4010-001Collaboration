#ward2dc.py

def ward2dc(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for char in s[::-1]:
        value = roman_dict[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    
    return result
roman_numeral = "XIV"
result = ward2dc(roman_numeral)
print(f"The integer representation of {roman_numeral} is: {result}")