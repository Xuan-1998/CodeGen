import sys

n = int(sys.stdin.readline())
dp = [[0] * (10**5 + 1) for _ in range(2)]

for i in range(n):
    t_i = int(sys.stdin.readline())
    j = min((t_i - 1) // 90, 6)  # at most 6 tickets of 90 minutes
    dp[0][j] += (t_i % 90 + 1)

for i in range(2):
    for j in range(10**5 + 1):
        if i > 0:
            j_prev = min((j - 1) // 90, 6)
            dp[i][j] = min(dp[(i-1)%2][j_prev*90+max(j%90-59, 0)], dp[i][j])
        else:
            dp[i][j] = max(20, (j % 60 + 1))

for _ in range(n):
    t_i = int(sys.stdin.readline())
    print(max(dp[1][t_i], dp[0][t_i]))
