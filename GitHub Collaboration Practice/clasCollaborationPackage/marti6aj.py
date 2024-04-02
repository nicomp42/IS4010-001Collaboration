#marti6aj.py
# Name: Andrew Martin
# email: marti6aj@mail.uc.edu
# Assignment Number: ClassColaborationPackage
# Due Date: April 2nd, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the module: Create a function with no parameters to call a Roman Numeral and convert it into an integer value.


def romanToInt() -> int:
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    s = "V"
    
    
    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    print(total)




