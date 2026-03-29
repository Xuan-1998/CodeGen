import sys

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]
b = [int(x) for x in sys.stdin.readline().split()]
c = [int(x) for x in sys.stdin.readline().split()]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(min(i, n), 0, -1):
        dp[i][j] = max(dp[i-1][j-1] + a[i-1], dp[i-1][j] + b[j-1])

print(max(sum(a_k for k in range(n)) - n, sum(c_k for c_k in range(1, n+1))), key=lambda x: x[0])
