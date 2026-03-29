from sys import stdin

n, t = map(int, stdin.readline().split())
fraction = stdin.readline().strip()

dp = [[0] * (t + 1) for _ in range(n + 1)]

for i in range(n + 1):
    if i == n:
        dp[i][0] = int(fraction)
    else:
        for j in range(t + 1):
            if i == 0:
                dp[i][j] = int(fraction[:i+1])
            elif j > 0:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] - (int(fraction[:i+1]) % 10))
                if i > 0 and j < t:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1])

print(max(dp[-1]))
