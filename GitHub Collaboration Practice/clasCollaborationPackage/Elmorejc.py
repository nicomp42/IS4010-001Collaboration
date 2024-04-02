#elmorejc.py

'''
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''

class Solution:
    def generate(self, numRows: int):
        result = []
        for i in range(numRows):
            row = [1]  # Initialize each row with 1
            for j in range(1, i):
                # Calculate the middle elements based on the previous row
                row.append(result[i - 1][j - 1] + result[i - 1][j])
            if i > 0:
                row.append(1)  # Add the last 1 to the row
            result.append(row)
        return result

# Example usage:
numRows = 7
solution = Solution()
output = solution.generate(numRows)
print(output)