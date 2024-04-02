#shermani.py
# main.py
# Name: Nosagie Sherman
# email: shermani@mail.uc.edu
# Assignment Number: Colboration
# Due Date: 4/2/2024
# Course/Section:  IS 4030 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Documentation
# Citations:
# Anything else that's relevant:
def is_ugly():
    num_print = 6
    num = 6
    if num <= 0:
        print("This number is not ugly")
    for prime in [2, 3, 5]:
        while num % prime == 0:
            num //= prime
    print("This number is very Ugly:", num_print)
