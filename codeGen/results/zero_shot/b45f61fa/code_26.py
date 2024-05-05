# Receive input for number of matrices (n) and dimensions (p)
import sys
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

# Create a table to store the minimum multiplications needed
dp = [[0] * len(p) for _ in range(len(p))]

# Fill the dp table using dynamic programming
for i in range(2, n):
    dp[i][i] = 0
    for j in range(i-1, -1, -1):
        dp[j][i] = float('inf')
        for k in range(j, i):
            q = p[k] * p[k+1]
            mult = dp[j][k] + dp[k+1][i] + p[j]*p[k+1]*q
            if mult < dp[j][i]:
                dp[j][i] = mult

# Construct the optimal parenthesization string
s = ''
for i in range(n-1):
    s += str(i) + ') * ('
for _ in range(n//2):
    s += 'A'

print(s)
