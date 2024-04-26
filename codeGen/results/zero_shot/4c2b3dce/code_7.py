def has_AB_and_BA(s):
    # Find the first occurrence of "AB"
    index_AB = s.find("AB")
    # If found, check if "BA" occurs after it
    if index_AB != -1 and "BA" in s[index_AB + 2:]:
        return "YES"
    
    # Find the first occurrence of "BA"
    index_BA = s.find("BA")
    # If found, check if "AB" occurs after it
    if index_BA != -1 and "AB" in s[index_BA + 2:]:
        return "YES"
    
    # If neither condition is met, return "NO"
    return "NO"

# Read input from stdin
s = input().strip()
# Output the result
print(has_AB_and_BA(s))
