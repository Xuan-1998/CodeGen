import sys

# Read input
n = int(input())
p = list(map(int, input().split()))

dp = [0] + [sys.maxsize]*(n+1)

for i in range(2, n+2):
    dp[i] = min(dp[j] + (1 if p[j-1] % 2 else 0) for j in range(i))

print((dp[n+1] + (1 if n % 2 else 0)) % 1000000007)
