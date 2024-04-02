# Name: Alyssa Battaglia
# email: battagaa@mail.uc.edu
# Assignment Number: InClassCollaboration
# Due Date: 04/02/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This module displays a function that takes letters and outputs the roman numeral number

# battagaa.py

def battagaa(s: str) -> int:
    '''
    Inputs a roman numeral letter and outputs a number
    @param: s, a string of letters, either I, V, X, L, C, D, or M.
    @return: result, the output number
    '''
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_values[char]
        if value >= prev_value:
            result += value
        else:
            result -= value
        prev_value = value
    
    return result
print(battagaa("III"))