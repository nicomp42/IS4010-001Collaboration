# walsh2ct.py
def walsh2ct():
    # Read the input string from user input
    s = input("Enter a string: ")

    # Trim the string
    s = s.strip()

    # If the string is empty, return 0
    if s == "":
        return 0

    # Split the string by spaces
    words = s.split()

    # Return the length of the last word
    return len(words[-1])

    # Call the function
    result = walsh2ct()
    print(f"Length of the last word: {result}")