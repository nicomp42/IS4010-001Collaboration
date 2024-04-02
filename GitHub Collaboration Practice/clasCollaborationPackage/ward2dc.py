#ward2dc.py
# Name:Duncan Ward
# email:ward2dc@mail.uc.edu
# Assignment Number: git hub collaboration 
# Due Date:/2/24
# Course/Section:4010 001
# Semester/Year:spring 2024
# Brief Description of the assignment: leetcode implementation 

# Brief Description of what this module does. converts Roman numerals to digits
# Citations: https://chat.openai.com/c/1cef1c34-9b1b-48d3-b096-22fc6a771e09
#https://leetcode.com/problems/roman-to-integer/description/
# Anything else that's relevant:
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

if __name__ == "__main__":
    roman_numeral = "XIV"
    result = ward2dc(roman_numeral)
    print(f"The integer representation of {roman_numeral} is: {result}")