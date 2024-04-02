#hill4ju.py

# Name: JaJuan Hill
# email: hill4ju@mail.uc.edu
# Assignment Number: ClassCollaboration 20240402
# Due Date: 4/2/2024
# Course/Section: IS 4010
# Semester/Year: Spring 2024
# Brief Description of the assignment:Collaborating on github

# Brief Description of what this module does: Creates a function with no parameters
# Citations:
# Anything else that's relevant:

    
def hill4ju():
    """
    Returns the number of '1' bits in the binary representation of a positive integer.
    """
    n = int(input("Enter a positive integer in binary format: "), 2)
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

if __name__ == "__main__":
    result = hill4ju()
    print(f"Number of set bits: {result}")