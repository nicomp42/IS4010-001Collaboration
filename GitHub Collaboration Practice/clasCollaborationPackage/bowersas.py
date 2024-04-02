'''
bowersas.py
'''
def bowersas(n):
    """
    Generate and print the first n rows of Pascal's Triangle
    """
    for i in range(1, n+1):
        C = 1  # used to represent C(line, i)
        for j in range(1, i+1):
            print(C, end=' ')
            C = C * (i - j) // j
        print()

# Example usage:
rows = 5
bowersas(rows)
