def contains_AB_and_BA(s):
    # Find the first occurrence of "AB"
    index_AB = s.find("AB")
    # If found, check for "BA" after it
    if index_AB != -1 and "BA" in s[index_AB + 2:]:
        return True

    # Find the first occurrence of "BA"
    index_BA = s.find("BA")
    # If found, check for "AB" after it
    if index_BA != -1 and "AB" in s[index_BA + 2:]:
        return True

    return False

# Read input from stdin
s = input().strip()

# Check for the non-overlapping substrings and print the result
print("YES" if contains_AB_and_BA(s) else "NO")
