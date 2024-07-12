python
def check_subsequences(s):
    n = len(s)
    
    found_AB = False
    found_BA = False
    
    # First, try finding "AB" followed by "BA"
    i = 0
    while i < n - 1:
        if s[i] == 'A' and s[i + 1] == 'B':
            found_AB = True
            i += 2  # Skip the next character to avoid overlap
            break
        i += 1
    
    while i < n - 1:
        if s[i] == 'B' and s[i + 1] == 'A':
            found_BA = True
            break
        i += 1
    
    if found_AB and found_BA:
        print("YES")
        return
    
    # Reset flags for the second check
    found_AB = False
    found_BA = False
    
    # Now, try finding "BA" followed by "AB"
    i = 0
    while i < n - 1:
        if s[i] == 'B' and s[i + 1] == 'A':
            found_BA = True
            i += 2  # Skip the next character to avoid overlap
            break
        i += 1
    
    while i < n - 1:
        if s[i] == 'A' and s[i + 1] == 'B':
            found_AB = True
            break
        i += 1
    
    if found_AB and found_BA:
        print("YES")
    else:
        print("NO")

# Read input from stdin
import sys
input = sys.stdin.read().strip()
check_subsequences(input)

