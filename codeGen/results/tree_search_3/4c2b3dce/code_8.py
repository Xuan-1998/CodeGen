def has_non_overlapping_AB(s):
    # Initialize a flag to check if we have found both substrings
    found = False

    # Iterate over the string s
    for i in range(len(s) - 1):
        # Check if we have 'AB' or 'BA' at this position
        if (s[i] == 'A' and s[i+1] == 'B') or (s[i] == 'B' and s[i+1] == 'A'):
            found = True

            # If we have found one, check if there is the other in the remaining string
            for j in range(i + 2, len(s) - 1):
                if (s[j] == 'A' and s[j+1] == 'B') or (s[j] == 'B' and s[j+1] == 'A'):
                    return "YES"

    # If we have not found both substrings, return "NO"
    if not found:
        return "NO"

# Read the string from standard input
s = input()

print(has_non_overlapping_AB(s))
