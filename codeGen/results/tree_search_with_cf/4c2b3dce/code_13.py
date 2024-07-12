def contains_non_overlapping_subsequences(s):
    n = len(s)
    found_AB = False
    found_BA = False
    pos_AB = -1
    pos_BA = -1

    # First pass to find the first occurrence of "AB" and "BA"
    for i in range(n - 1):
        if s[i:i+2] == "AB" and not found_AB:
            found_AB = True
            pos_AB = i
        if s[i:i+2] == "BA" and not found_BA:
            found_BA = True
            pos_BA = i

    # Check for non-overlapping condition
    if found_AB and found_BA:
        if pos_AB + 1 < pos_BA or pos_BA + 1 < pos_AB:
            return "YES"

    # Reset for second pass to ensure non-overlapping check again
    found_AB = False
    found_BA = False

    # Second pass to ensure non-overlapping
    for i in range(n - 1):
        if s[i:i+2] == "AB":
            if found_BA and i > pos_BA + 1:
                return "YES"
            found_AB = True
            pos_AB = i
        if s[i:i+2] == "BA":
            if found_AB and i > pos_AB + 1:
                return "YES"
            found_BA = True
            pos_BA = i

    return "NO"

# Read input from stdin
import sys
input = sys.stdin.read().strip()

# Get the result
result = contains_non_overlapping_subsequences(input)

# Print the result
print(result)

