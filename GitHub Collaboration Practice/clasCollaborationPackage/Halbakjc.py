#Halbakjc,py

def halbakjc(x: int) -> int:
    '''
     Calculates the integer square root of a non-negative integer.

    Args:
        x (int): A non-negative integer for which to find the square root.

    Returns:
        int: The integer part of the square root, rounded down.
(problem 69)
    '''
    if x == 0:
        return 0

    left, right = 0, x
    while left < right:
        mid = (left + right + 1) // 2
        if mid > x // mid:
            right = mid - 1
        else:
            left = mid

    return left

# Example usage:
print(halbakjc(4))  # Output: 2
print(halbakjc(8))  # Output: 2