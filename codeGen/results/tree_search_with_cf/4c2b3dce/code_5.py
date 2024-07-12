def contains_AB_and_BA(s):
    n = len(s)
    if n < 2:
        return "NO"
    
    found_AB = False
    found_BA = False
    
    i = 0
    while i < n - 1:
        if s[i:i+2] == "AB":
            if found_BA:
                return "YES"
            found_AB = True
            i += 2  # Skip the next character to ensure non-overlapping
        elif s[i:i+2] == "BA":
            if found_AB:
                return "YES"
            found_BA = True
            i += 2  # Skip the next character to ensure non-overlapping
        else:
            i += 1
    
    return "NO"

# Read input from stdin
import sys
input = sys.stdin.read().strip()
print(contains_AB_and_BA(input))

