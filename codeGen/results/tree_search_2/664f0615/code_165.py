from sys import stdin

def max_path_length(v0, vf, t, delta):
    dp = [[0] * (t + 1) for _ in range(t + 1)]

    for i in range(1, t + 1):
        for j in range(1, t + 1):
            if i == j:
                dp[i][j] = min(vf, v0 + (i - 1) * delta)
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] + delta)

    return dp[t][t]

v0, vf = map(int, stdin.readline().split())
t, delta = map(int, stdin.readline().split())

print(max_path_length(v0, vf, t, delta))
