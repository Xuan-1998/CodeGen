def contains_AB_and_BA(s):
    # Step 1: Find "AB"
    index_AB = s.find("AB")
    if index_AB != -1:
        # Step 2: Look for "BA" after "AB"
        if "BA" in s[index_AB + 2:]:
            return "YES"
    
    # Step 3: Reset search and look for "BA"
    index_BA = s.find("BA")
    if index_BA != -1:
        # Step 5: Look for "AB" after "BA"
        if "AB" in s[index_BA + 2:]:
            return "YES"
    
    # Step 6: If neither found, return "NO"
    return "NO"

# Read input string from stdin
input_string = input().strip()

# Print the result
print(contains_AB_and_BA(input_string))
