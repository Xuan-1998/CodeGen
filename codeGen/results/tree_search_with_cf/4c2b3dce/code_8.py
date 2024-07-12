python
def check_subsequences(s):
    n = len(s)
    found_AB = False
    found_BA = False
    
    i = 0
    while i < n - 1:
        if s[i:i+2] == "AB":
            if found_BA:
                print("YES")
                return
            found_AB = True
            i += 2  # Skip the next character to ensure non-overlapping
        elif s[i:i+2] == "BA":
            if found_AB:
                print("YES")
                return
            found_BA = True
            i += 2  # Skip the next character to ensure non-overlapping
        else:
            i += 1
    
    print("NO")

# Read input from stdin
import sys
input = sys.stdin.read().strip()

# Call the function with the input string
check_subsequences(input)

