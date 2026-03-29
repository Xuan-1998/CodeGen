import sys

# Read the input
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Define a function to solve the problem
def solve(n, k, s):
    # If k is greater than or equal to n, we can just duplicate the string
    if k >= n:
        return s * ((k + n - 1) // n)
    
    # If k is less than n, we need to decide whether to delete the last character
    # or duplicate the string up to length k
    if s[-1] <= s[k-1]:
        return s[:k]
    else:
        return s[:-1]

# Print the solution
print(solve(n, k, s))
