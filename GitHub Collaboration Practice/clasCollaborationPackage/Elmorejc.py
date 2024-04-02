#elmorejc.py

#main.py
# Name: Jake Elmore
# email: Elmorejc@mail.uc.edu
# Assignment Number: Inclass4/2/2024
# Due Date: 4/2/2024
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Solves pascal's triangle
# Brief Description of what this module does Solve's pascal's triangle
# Citations: 
# Anything else that's relevant:

def generate_pascals_triangle():
    numRows = 5  # You can adjust this number as needed
    
    triangle = [[1]]
    for i in range(1, numRows):
        prev_row = triangle[i - 1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)
    
    return triangle

# Test the function
print(generate_pascals_triangle())