def maximum_length(v1, v2, t, delta):
    dp = [[0] * (v2 + 1) for _ in range(t + 1)]

    for i in range(1, t + 1):
        for speed in range(1, v2 + 1):
            if speed == v1 or speed == v2:
                dp[i][speed] = min(max(i - 1, 0), t)
            else:
                dp[i][speed] = max(dp[i-1][speed-delta], dp[i-1][speed+delta])

    return max(dp[-1])

# Read input from stdin
v1, v2 = map(int, input().split())
t, delta = map(int, input().split())

print(maximum_length(v1, v2, t, delta))
