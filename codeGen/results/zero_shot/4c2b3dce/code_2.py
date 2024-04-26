def check_substrings(s):
    # First, check for "AB" followed by "BA"
    ab_index = s.find("AB")
    while ab_index != -1:
        # Check if there's a "BA" following "AB"
        ba_index = s.find("BA", ab_index + 2)
        if ba_index != -1:
            return "YES"
        # Move to the next occurrence of "AB"
        ab_index = s.find("AB", ab_index + 1)

    # Next, check for "BA" followed by "AB"
    ba_index = s.find("BA")
    while ba_index != -1:
        # Check if there's an "AB" following "BA"
        ab_index = s.find("AB", ba_index + 2)
        if ab_index != -1:
            return "YES"
        # Move to the next occurrence of "BA"
        ba_index = s.find("BA", ba_index + 1)

    return "NO"

# Read input from stdin
s = input().strip()
# Output the result
print(check_substrings(s))
