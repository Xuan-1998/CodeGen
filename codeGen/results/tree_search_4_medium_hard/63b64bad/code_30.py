import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

dp = [[False] * (10**9 + 1) for _ in range(n + 1)]
y_values = []

for i in range(2, n + 1):
    x = 1
    y = 0
    while x <= n and x > 0:
        dp[i][x + seq[x - 1] - 1] = True
        x += seq[x - 1]
        y += seq[x - 1]
        x -= seq[x - 1]

    if x <= 0 or x > n:
        y_values.append(y)
    else:
        y_values.append(-1)

print(*y_values, sep='\n')
