def has_non_overlapping_AB_and_BA(s):
    # Search for "AB" followed by "BA"
    pos_AB = s.find("AB")
    if pos_AB != -1 and "BA" in s[pos_AB+2:]:
        return "YES"

    # Search for "BA" followed by "AB"
    pos_BA = s.find("BA")
    if pos_BA != -1 and "AB" in s[pos_BA+2:]:
        return "YES"

    return "NO"

# Read input from stdin
s = input().strip()

# Output the result to stdout
print(has_non_overlapping_AB_and_BA(s))
