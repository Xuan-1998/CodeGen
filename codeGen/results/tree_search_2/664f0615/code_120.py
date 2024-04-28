def max_distance(v0, vf, t, dv):
    dp = [[0] * (t + 1) for _ in range(101)]
    for v in range(min(v0, vf), max(v0, vf) + 1):
        dp[v][0] = 0
        for i in range(t):
            if i == 0:
                dp[v][i+1] = dp[v][i]
            else:
                if abs(v - dp[int((v + v0) / 2)][i]) <= dv:
                    dp[v][i+1] = max(dp[v][i], dp[int((v + v0) / 2)][i] + (vf - v0) / (t-1))
                else:
                    dp[v][i+1] = dp[v][i]
    return max(dp[i][t] for i in range(min(v0, vf), max(v0, vf) + 1))

v0, vf, t, dv = [int(x) for x in input().split()]
print(max_distance(v0, vf, t, dv))
