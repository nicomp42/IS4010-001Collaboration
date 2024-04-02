#Given a string s consisting of words and spaces, return the length of the last word in the string.
def last_word_length(string):
    return len(string.rsplit(' ', 1)[-1])
# Example usage:
print(last_word_length('Hello World'))  # Output: 5