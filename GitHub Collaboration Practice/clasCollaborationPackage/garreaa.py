#garreaa.py
# Name: Aanika Garre
# email: garreaa@mail.uc.edu
# Assignment Number: InClass_20240402
# Due Date: 4/2/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment focuses on GitHub collaboration.

# Brief Description of what this module does: This module creates a function that returns the length of the last word in a string.
# Citations:
# Anything else that's relevant:

#LengthofLastWord
def garreaa() -> int:
    """
    Returns the length of the last word in the given string 's'.
    """
    # Remove trailing spaces
    s = "I'm so confused"
    s = s.rstrip()
    if not s:
        return 0  # Empty string

    # Split the string by spaces and return the length of the last word
    words = s.split()
    print(len(words[-1]))
