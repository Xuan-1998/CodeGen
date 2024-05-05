import sys

# Read input from stdin
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

if k <= n:
    # Delete the last character if k is less than or equal to n
    result = s[:-1]
else:
    # Duplicate the string and trim it to length k
    result = s * (k // len(s)) + s[:k % len(s)]

# Print the result to stdout
print(result)
