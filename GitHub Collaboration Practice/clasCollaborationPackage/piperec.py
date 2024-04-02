#piperec.py
# Name: Elizabeth Piper
# email: piperec@mail.uc.edu
# Assignment Number: Assignment Collaboration Practice
# Due Date: 4/2/2024
# Course/Section: IS 4010 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Find a function from leetcode

# Brief Description of what this module does: This module is to count the elements in the last word
# Citations:
# Anything else that's relevant:

def piperec():
    # Example input string
    s = "Given a string s consisting of words and spaces, return the length of the last word in the string."
    
    # Remove trailing and leading white spaces
    s = s.strip()
    
    # Split the string by spaces
    words = s.split()
    
    # Check if there are any words in the string
    if len(words) == 0:
        print("No words found.")
        return 0
    
    # Calculate the length of the last word
    last_word_length = len(words[-1])
    
    # Print the length of the last word
    print("Length of the last word:", last_word_length)
    
    # Return the length of the last word
    return last_word_length
print(piperec())

