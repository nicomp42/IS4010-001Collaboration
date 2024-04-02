# Name: Mikaela Teowratanakul
# email: teowramm@mail.uc.edu
# Assignment Number: In class 04/02/24
# Due Date: 04/02/24
# Course/Section: IS4010 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Display your understanding of collaboration on github and eclipse
# Brief Description of what this module does: Displays my understanding of collaborating on github and eclipse
# Citations: N/A
# Anything else that's relevant: N/A


# i did problem #125 on leetcode

def teowramm():
    input_string = "A man, a plan, a canal: Panama"
    cleaned_s = ''.join(c.lower() for c in input_string if c.isalnum())
    return cleaned_s == cleaned_s[::-1]

# Example usage:
result = teowramm()

if __name__ == "__main__":
    print(f"Is the input string a valid palindrome? {result}")