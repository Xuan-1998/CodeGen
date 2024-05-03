from io import StringIO
import sys

input_stream = StringIO(sys.stdin.read())
sys.stdin = input_stream

n, m = map(int, input().split())
dp = [[0] * m for _ in range(m)]

for i in range(n):
    species, x = map(int, input().split())
    for j in range(1, m+1):
        if dp[species-1][j-1] < dp[species-1][j]:
            dp[species-1][j] = dp[species-1][j-1]
    dp[species-1][species-1] += 1

print(sum(max(0, dp[i][j]-dp[i][k]) for i in range(m) for j in range(i+1)))
