python
def check_subsequences(s: str) -> str:
    n = len(s)
    
    # Early exit if the string is too short
    if n < 4:
        return "NO"
    
    # Flags to indicate if we found the subsequences
    found_AB = False
    found_BA = False
    
    # Check for "AB" followed by "BA"
    i = 0
    while i < n - 1:
        if s[i:i+2] == "AB":
            found_AB = True
            i += 2  # Skip the next character to avoid overlap
            break
        i += 1
    
    while i < n - 1:
        if s[i:i+2] == "BA":
            found_BA = True
            break
        i += 1
    
    if found_AB and found_BA:
        return "YES"
    
    # Reset flags for the second check
    found_AB = False
    found_BA = False
    
    # Check for "BA" followed by "AB"
    i = 0
    while i < n - 1:
        if s[i:i+2] == "BA":
            found_BA = True
            i += 2  # Skip the next character to avoid overlap
            break
        i += 1
    
    while i < n - 1:
        if s[i:i+2] == "AB":
            found_AB = True
            break
        i += 1
    
    if found_AB and found_BA:
        return "YES"
    
    return "NO"

# Read input from stdin
import sys
input = sys.stdin.read().strip()
print(check_subsequences(input))

