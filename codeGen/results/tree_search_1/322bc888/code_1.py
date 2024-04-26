import sys

# Function to calculate the cost to make the substring beautiful
def calculate_cost(s, l, r):
    # Initialize the cost to 0
    cost = 0
    # Iterate over the substring
    for i in range(l, r):
        # Check for palindrome of length 2
        if s[i] == s[i+1]:
            cost += 1
            # Skip the next character since we've already changed it
            i += 1
        # Check for palindrome of length 3
        elif i+2 < r and s[i] == s[i+2]:
            cost += 1
            # Skip the next two characters since we've changed one of them
            i += 2
    return cost

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Process each query
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    # Adjust indices to be zero-based
    l -= 1
    r -= 1
    # Calculate and print the cost for this query
    print(calculate_cost(s, l, r))
