def has_non_overlapping_substrings(s):
    # Search for "AB" then "BA"
    index_ab = s.find("AB")
    if index_ab != -1:
        if "BA" in s[index_ab+2:]:
            return "YES"
    # Search for "BA" then "AB"
    index_ba = s.find("BA")
    if index_ba != -1:
        if "AB" in s[index_ba+2:]:
            return "YES"
    return "NO"

# Read input from stdin
s = input().strip()
# Output the result
print(has_non_overlapping_substrings(s))
