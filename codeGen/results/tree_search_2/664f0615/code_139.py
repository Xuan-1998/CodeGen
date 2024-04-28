from sys import stdin

def solve():
    init_speed, final_speed = map(int, stdin.readline().split())
    time_to_travel, max_change = map(int, stdin.readline().split())

    dp = [[0] * (time_to_travel + 1) for _ in range(final_speed - init_speed + 1)]

    for i in range(1, final_speed - init_speed + 1):
        for j in range(1, time_to_travel + 1):
            if i <= time_to_travel and abs(i - j) <= max_change:
                dp[i][j] = min(dp[i-1][j-1], (i-j) * (init_speed + i // 2))
            else:
                dp[i][j] = dp[i-1][j]

    return dp[final_speed - init_speed][time_to_travel]

print(solve())
