import sys

# Function to calculate the cost to make the substring beautiful
def calculate_cost(s, l, r):
    cost = 0
    for i in range(l, r):
        if s[i] == s[i+1]:
            cost += 1
    return cost

# Read input from stdin
n, m = map(int, sys.stdin.readline().strip().split())
s = sys.stdin.readline().strip()

# Process each query
for _ in range(m):
    l, r = map(int, sys.stdin.readline().strip().split())
    # Adjust indices for 0-based indexing
    l -= 1
    r -= 1
    # Calculate and print the cost
    print(calculate_cost(s, l, r))
