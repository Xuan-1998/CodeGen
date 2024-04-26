def contains_non_overlapping_substrings(s):
    # Search for "AB" followed by "BA"
    index_ab = s.find('AB')
    if index_ab != -1:
        index_ba = s.find('BA', index_ab + 2)
        if index_ba != -1:
            return "YES"
    
    # Search for "BA" followed by "AB"
    index_ba = s.find('BA')
    if index_ba != -1:
        index_ab = s.find('AB', index_ba + 2)
        if index_ab != -1:
            return "YES"
    
    return "NO"

# Read input from stdin
s = input().strip()
# Check for non-overlapping substrings and print the result to stdout
print(contains_non_overlapping_substrings(s))
