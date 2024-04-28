code = '''
import sys

m, N = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(m+1)]

for i in range(1, m+1):
    for n in range(N+1):
        dp[i][n] = dp[i-1][n]
        if n <= N and n == sum(arr[:i]):
            dp[i][n] += 1
        elif N > n:
            dp[i][n] += dp[i-1][n+arr[i]]

print(dp[m][N] % (10**9 + 7))
'''

