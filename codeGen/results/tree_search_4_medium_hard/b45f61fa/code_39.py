import sys

n = int(input())  # Read the number of matrices from standard input
p = list(map(int, input().split()))  # Read the dimensions of the matrices

# Initialize the dynamic programming table with infinity
dp = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    dp[0][i] = i  # Base case: multiplying matrix 1 with all subsequent matrices

for L in range(2, n+1):
    for i in range(n-L+1):
        j = i + L - 1
        for k in range(i, j):
            dp[i][j] = min(dp[0][i-1], dp[i][k] + dp[k+1][j]) + p[i]*p[k+1]*p[j]

# Find the minimum number of multiplications needed to multiply all matrices
min_multiplications = sys.maxsize
for i in range(1, n):
    min_multiplications = min(min_multiplications, dp[0][i-1] + dp[i][n-1])

print(min_multiplications)  # Print the answer to standard output
