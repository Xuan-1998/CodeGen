def has_non_overlapping_substrings(s):
    for i in range(len(s) - 2):  # Window size is 3
        if s[i:i+2] == "AB" and s[i+2:] == "BA":
            return "YES"
    return "NO"

# Read the input string from stdin
s = input()

print(has_non_overlapping_substrings(s))
