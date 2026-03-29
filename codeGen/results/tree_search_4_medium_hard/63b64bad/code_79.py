n = int(input())
seq = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    x, y = 1, 0
    while x <= n and x > 0:
        if seq[x-1] + y > n or seq[x-1] + y < 1:
            break
        x += seq[x-1]
        y += seq[x-1]

    dp[n-i-1][y] = 1

print(-1 if not any(dp[-1]) else max(range(len(dp[-1])))[0])
