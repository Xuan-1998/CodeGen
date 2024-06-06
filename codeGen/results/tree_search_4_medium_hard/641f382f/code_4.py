import math
from sys import stdin

# Function to compute GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Read input
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

# Initialize dp and gcd arrays
dp = [[float('inf')] * n for _ in range(n)]
gcd_array = [[0] * n for _ in range(n)]

# Precompute gcd for all subarrays
for i in range(n):
    gcd_array[i][i] = arr[i]
    for j in range(i + 1, n):
        gcd_array[i][j] = gcd(gcd_array[i][j - 1], arr[j])

# Fill dp array
for i in range(n):
    dp[i][i] = 0
    if i < n - 1:
        dp[i][i + 1] = 1 if gcd_array[i][i + 1] == 1 else float('inf')

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if gcd_array[i][j] == 1:
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)

# Check if it's possible to make all elements equal to 1
if dp[0][n - 1] == float('inf'):
    print(-1)
else:
    print(dp[0][n - 1])
