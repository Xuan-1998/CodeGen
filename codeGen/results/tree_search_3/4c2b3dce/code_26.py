def has_ab_ba(s):
    # Check for "AB" and store its index
    ab_index = s.find("AB")
    
    if ab_index != -1:
        # If "AB" is found, check for "BA" in the remaining string
        remaining_string = s[ab_index+2:]
        ba_index = remaining_string.find("BA")
        
        # Return "YES" if both substrings are found
        return "YES" if ba_index != -1 else "NO"
    
    # If no "AB", check for "BA" and store its index
    ba_index = s.find("BA")
    
    if ba_index != -1:
        # If "BA" is found, check for "AB" in the remaining string
        remaining_string = s[ba_index+2:]
        ab_index = remaining_string.find("AB")
        
        # Return "YES" if both substrings are found
        return "YES" if ab_index != -1 else "NO"
    
    # If neither "AB" nor "BA" is found, return "NO"
    return "NO"

# Read input from standard input
s = input()

# Print the answer to standard output
print(has_ab_ba(s))
