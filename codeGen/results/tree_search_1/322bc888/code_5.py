import sys

# Function to calculate the cost to make a substring non-palindromic
def calculate_cost(s, l, r):
    # If the length of the substring is 1, no operation is needed
    if r - l == 0:
        return 0
    # If the length is 2 and both characters are the same, we need 1 operation
    if r - l == 1 and s[l] == s[r]:
        return 1
    # If the length is 3, we check if it's a palindrome
    if r - l == 2 and s[l] == s[r]:
        return 1
    # For longer substrings, we can alternate between 'a' and 'b'
    # Hence, at most 1 operation is needed for any pair of adjacent characters
    return (r - l + 1) // 2

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Process each query
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    # Adjust indices to be zero-based
    l -= 1
    r -= 1
    # Calculate and print the cost
    print(calculate_cost(s, l, r))
