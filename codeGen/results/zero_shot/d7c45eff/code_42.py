import sys

# Read input from stdin
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# If k is less than or equal to n, decide whether to delete the last character or duplicate the string
if k <= n:
    if k == n:  # If k equals n, just take the original string
        result = s
    elif k < n:  # If k is less than n, delete the last character
        result = s[:-1]
    else:  # If k equals n+1, duplicate the string and remove the last character
        result = s + s[:-1]

# If k is greater than n, simply duplicate the input string until it reaches a length of k
else:
    result = (s * ((k - n) // len(s)) + s[:((k - n) % len(s))])

# Print the result to stdout
print(result)
