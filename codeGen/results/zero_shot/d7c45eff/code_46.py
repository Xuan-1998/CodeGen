import sys

def solve(n, k, s):
    # If the desired length is less than or equal to the original length,
    # we can simply truncate the original string.
    if k <= n:
        return s[:k]
    
    # If the desired length is greater than the original length,
    # we need to consider deleting the last character or duplicating the string.
    else:
        # Delete the last character
        deleted = s[:-1]
        
        # Duplicate the original string
        duplicated = s + s
        
        # Compare the lexicographical order of the three strings
        if deleted < s < duplicated:
            return deleted[:k]
        elif s < duplicated:
            return s[:k]
        else:
            return duplicated[:k]

# Read input from stdin
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Print the solution to stdout
print(solve(n, k, s))
