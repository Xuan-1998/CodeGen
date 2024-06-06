import math
from sys import stdin

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Initialize the DP array with infinity
dp = [[float('inf')] * n for _ in range(n)]

# Base case for single elements
for i in range(n):
    dp[i][i] = 0

# Check if the array already contains a 1
if 1 in arr:
    print(0)
else:
    # Check if it is impossible to reduce the array to all 1s
    array_gcd = arr[0]
    for num in arr:
        array_gcd = gcd(array_gcd, num)
    if array_gcd > 1:
        print(-1)
    else:
        # DP computation
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    left_gcd = gcd(arr[i], arr[k])
                    right_gcd = gcd(arr[k + 1], arr[j])
                    if left_gcd == 1 or right_gcd == 1:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)

        # Check if the entire array can be reduced to 1
        if dp[0][n - 1] == float('inf'):
            print(-1)
        else:
            print(dp[0][n - 1])
