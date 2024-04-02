# Name: Binta Drammeh
# email: Drammeba@mail.uc.edu
# Assignment Number: In class Assignment
# Due Date: April 2nd, 2024
# Course/Section: IS 4030 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: add leetcode problem into a new module
# Citations: 
# Anything else that's relevant:

#drammeba.py

def max_profit():
    # Example stock prices
    prices = [7, 1, 5, 3, 6, 4]
    
    # Initialize variables to keep track of minimum price and maximum profit
    min_price = float('inf')
    max_profit = 0
    
    # Iterate through the prices
    for price in prices:
        # Update the minimum price
        min_price = min(min_price, price)
        # Update the maximum profit
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

# Example usage
if __name__ == "__main__":  
        #Entry point code goes here 
    print(f"Max profit: {max_profit()}")