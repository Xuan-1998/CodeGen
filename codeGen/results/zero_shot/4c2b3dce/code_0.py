def check_AB_BA(s):
    # Find "AB" and "BA" in the string s
    ab_index = -1  # Initialize to -1 (not found)
    ba_index = -1  # Initialize to -1 (not found)
    
    for i in range(len(s) - 1):
        if s[i:i+2] == "AB" and (ab_index == -1 or i - ba_index > 1):
            ab_index = i
        elif s[i:i+2] == "BA" and (ba_index == -1 or i - ab_index > 1):
            ba_index = i
        
        # If both are found and non-overlapping, return "YES"
        if ab_index != -1 and ba_index != -1:
            return "YES"
    
    return "NO"

# Read input from stdin
s = input().strip()
# Print the output
print(check_AB_BA(s))
