#howardgy.py

def howardgy():
    '''
    Leet Code Problem 136: Single Number
    @return A single number
    '''
    nums = [2, 2, 1]  # Example input array

    # XOR all elements in the array
    result = 0
    for num in nums:
        result ^= num
    
    return result

if __name__ == "__main__":
    print(howardgy())
    