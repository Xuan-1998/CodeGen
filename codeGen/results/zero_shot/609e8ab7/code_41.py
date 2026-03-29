import sys

def solve(n, parent, ranges):
    # Initialize dp array with infinite values
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Root node has no operations needed

    for i in range(1, n + 1):
        l, r = ranges[i - 1]
        min_val = max(l, int((l + r) / 2))  # Calculate minimum value
        if dp[parent[i - 1]] + (min_val - dp[i]) > 0:
            # Add operations to bring the vertex's value up to min_val
            dp[i] = min_val

    return sum(dp[1:])

# Read input from stdin
n = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
ranges = []
for _ in range(n):
    l, r = map(int, sys.stdin.readline().split())
    ranges.append((l, r))

# Print the minimum number of operations needed
print(solve(n, parent, ranges))
