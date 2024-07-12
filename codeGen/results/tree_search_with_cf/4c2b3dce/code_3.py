python
def contains_non_overlapping_subsequences(s):
    n = len(s)
    
    # Check for "AB" followed by "BA"
    found_AB = False
    for i in range(n - 1):
        if not found_AB and s[i] == 'A' and s[i + 1] == 'B':
            found_AB = True
            i += 1  # Skip to the next character after "AB"
        elif found_AB and s[i] == 'B' and s[i + 1] == 'A':
            print("YES")
            return
    
    # Check for "BA" followed by "AB"
    found_BA = False
    for i in range(n - 1):
        if not found_BA and s[i] == 'B' and s[i + 1] == 'A':
            found_BA = True
            i += 1  # Skip to the next character after "BA"
        elif found_BA and s[i] == 'A' and s[i + 1] == 'B':
            print("YES")
            return
    
    print("NO")

# Read input from stdin
import sys
input = sys.stdin.read().strip()
contains_non_overlapping_subsequences(input)

