# Name: Anna Moorhead
# email: moorheaa@mail.uc.edu
# Assignment Number: GitHub Collaboration Practice
# Due Date: April 2, 2024
# Course/Section: IS 4010 - 001
# Semester/Year: Spring 2024
# Brief Description of the assignment:
# Citations:
# Anything else that's relevant:

# moorheaa.py

def length_of_last_word(s: str) -> int:
    '''
    Problem 58. Length of Last Word (on LeetCode)
    You will write a word/ sentence and the function will determine how many letters are in the last word
    @param s: str: one or more English words with spaces in between 
    @return: the length of the last word in the string
    '''
    # Remove trailing spaces from the string
    s = s.rstrip()
    
    # Find the last space in the modified string
    last_space_index = s.rfind(' ')
    
    # Extract the last word using slicing
    last_word = s[last_space_index + 1:] if last_space_index != -1 else s
    
    # Return the length of the last word
    return len(last_word)

# Example usage:
s1 = "Hello World"
s2 = "fly me tothe moon  "
s3 = "luffy is still joyboy"

if __name__ == "__main__":
    print(length_of_last_word(s1))  # Output: 5
    print(length_of_last_word(s2))  # Output: 4
    print(length_of_last_word(s3))  # Output: 6