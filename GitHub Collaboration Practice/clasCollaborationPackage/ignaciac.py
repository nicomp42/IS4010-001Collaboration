# ignaciac.py

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  # Initialize an empty stack to keep track of characters
        
        for char in s:
            # Check if the stack is not empty and the current character cancels the top character
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()  # Remove the top character from the stack
            else:
                stack.append(char)  # Otherwise, add the current character to the stack
        
        # Join the characters left in the stack to form the modified string
        return ''.join(stack)

# Example usage:
solution = Solution()
print(solution.makeGood("leEeetcode"))  # Output: "leetcode"
