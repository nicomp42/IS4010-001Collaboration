#roopna.py
def roopnacn():
    s = "egg"
    t = "add"

    if len(s) != len(t):
        print("Input strings are not of equal length.")
        return

    # Create dictionaries to store character mappings
    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        char_s, char_t = s[i], t[i]

        # Check if the mapping already exists
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                print("Not isomorphic.")
                return
        else:
            s_to_t[char_s] = char_t

        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                print("Not isomorphic.")
                return
        else:
            t_to_s[char_t] = char_s

    print("Isomorphic!")

# Example usage
roopnacn()  # Output: Isomorphic!
