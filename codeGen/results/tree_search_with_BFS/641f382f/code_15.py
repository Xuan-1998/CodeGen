import sys
from math import gcd

# Function to compute the GCD of a subarray
def compute_gcd(i, j):
    return gcd(a[i], dp[i+1][j]) if i < j else a[i]

# Read input
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# Check if there's a 1 in the array
if 1 in a:
    print(n - a.count(1))
    sys.exit()

# Initialize the dp array
dp = [[0]*n for _ in range(n)]

# Fill the dp array
for length in range(1, n):
    for i in range(n - length):
        j = i + length
        dp[i][j] = compute_gcd(i, j)
        if dp[i][j] == 1:
            dp[i][j] = length

# Find the minimum value in the dp array
min_value = min(min(row) for row in dp if row)

# Print the result
print(min_value + n if min_value else -1)

