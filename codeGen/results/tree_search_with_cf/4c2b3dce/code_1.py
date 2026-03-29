def check_subsequences(s):
    n = len(s)
    
    # First pass: check for "AB" followed by "BA"
    found_AB = False
    for i in range(n - 1):
        if not found_AB and s[i:i+2] == "AB":
            found_AB = True
            i += 1  # Move past "AB"
        elif found_AB and s[i:i+2] == "BA":
            print("YES")
            return
    
    # Reset and check for "BA" followed by "AB"
    found_BA = False
    for i in range(n - 1):
        if not found_BA and s[i:i+2] == "BA":
            found_BA = True
            i += 1  # Move past "BA"
        elif found_BA and s[i:i+2] == "AB":
            print("YES")
            return
    
    print("NO")

# Read input from stdin
import sys
input = sys.stdin.read().strip()

# Call the function with the input string
check_subsequences(input)

