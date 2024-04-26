def contains_AB_and_BA(s):
    # First, search for "AB" followed by "BA"
    ab_index = s.find("AB")
    while ab_index != -1:
        # Start searching for "BA" after the "AB" we've found
        ba_index = s.find("BA", ab_index + 2)
        if ba_index != -1:
            return "YES"
        # Continue searching for the next "AB"
        ab_index = s.find("AB", ab_index + 1)

    # Now, search for "BA" followed by "AB"
    ba_index = s.find("BA")
    while ba_index != -1:
        # Start searching for "AB" after the "BA" we've found
        ab_index = s.find("AB", ba_index + 2)
        if ab_index != -1:
            return "YES"
        # Continue searching for the next "BA"
        ba_index = s.find("BA", ba_index + 1)

    return "NO"

# Read input from stdin
s = input().strip()

# Output the result
print(contains_AB_and_BA(s))
