import sys

def solve():
    s = input()
    n = len(s)
    
    # Base case: length of string is less than 3
    if n < 3:
        return "NO" if not (s == 'AB' or s == 'BA') else "YES"
    
    # Initialize variables
    found_AB = False
    found_BA = False
    
    # Iterate over the string
    for i in range(n-1):
        # Check for "AB" and "BA" substrings
        if s[i:i+2] == 'AB' and not found_AB:
            found_AB = True
        elif s[i:i+2] == 'BA' and not found_BA:
            found_BA = True
        
        # If we've found both, exit the loop
        if found_AB and found_BA:
            break
    
    return "YES" if found_AB and found_BA else "NO"

print(solve())
