def contains_AB_and_BA(s):
    # Search for "AB" followed by "BA"
    pos_AB = s.find("AB")
    if pos_AB != -1:
        # Start searching for "BA" from the position right after "AB"
        if s.find("BA", pos_AB + 2) != -1:
            return "YES"

    # Search for "BA" followed by "AB"
    pos_BA = s.find("BA")
    if pos_BA != -1:
        # Start searching for "AB" from the position right after "BA"
        if s.find("AB", pos_BA + 2) != -1:
            return "YES"

    return "NO"

# Read input from stdin
s = input().strip()
# Print the result to stdout
print(contains_AB_and_BA(s))
