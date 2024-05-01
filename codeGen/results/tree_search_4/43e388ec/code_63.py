def solve():
    a, b = map(int, input().split())
    dp = [[0] * (len(bin(a)) - 2) for _ in range(315)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i > 0 and j < len(dp[0]) - 1:
                dp[i][j] = dp[i-1][(j+1)%len(dp[0])] ^ ((b >> (i%len(dp[0])))&1)
            elif i == 0:
                dp[i][j] = a & (1 << j) and b >> j or a
    return sum(sum(row) for row in dp) % (10**9 + 7)

print(solve())
