n = int(input())  # Read the number of rooms
p = list(map(int, input().split()))  # Read the portals

dp = [[0] * 2 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == 1:
        dp[i][0] = 0
    else:
        for s in range(2):
            if s == 0:  # First portal used
                dp[i][s] = 1 + min(dp[j][0] for j in range(1, i) if p[j - 1] == i - 1)
            else:  # Second portal used
                dp[i][s] = 1 + min(dp[j][1] for j in range(i + 1, n + 2) if p[j - 1] == i)

print((dp[n + 1][0]) % (10**9 + 7))
