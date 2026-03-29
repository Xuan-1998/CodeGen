dp = [[float('inf')] * (s + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(s + 1):
        if i == 1:
            dp[i][j] = min((x + y) for x in range(max(0, s - a1)) + 1 for y in range(a1 - (s - max(0, s - a1))) + 1)
        else:
            for xi in range(min(j, a1), -1, -1):
                yi = a1 - xi
                if yi >= 0 and yi <= j:
                    dp[i][j] = min(dp[i][j], xi * (dp_prev[1][j - a1 + i]) + yi)
    dp_prev = dp

print(min(dp[-1]))
