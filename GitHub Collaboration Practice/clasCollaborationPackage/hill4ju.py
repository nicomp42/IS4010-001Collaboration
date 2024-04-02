#hill4ju.py

def hill4ju(roman):
    roman_numerals = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    
    result = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i+2] in roman_numerals:
            result += roman_numerals[roman[i:i+2]]
            i += 2
        else:
            result += roman_numerals[roman[i]]
            i += 1
    
    return result

roman_numeral = "XXIII"  # Replace with your desired Roman numeral
integer_value = hill4ju(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}")