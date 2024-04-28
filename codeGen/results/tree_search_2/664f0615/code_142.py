import sys

def max_distance(initial_speed, final_speed, time_change):
    dp = [[0] * (final_speed + 1) for _ in range(time_change + 1)]

    for i in range(time_change + 1):
        for j in range(final_speed + 1):
            if i == 0:
                dp[i][j] = 0
            elif j == initial_speed:
                dp[i][j] = min(dp[i - 1][k] + abs(k - j) * (i if k != 0 else 1) for k in range(final_speed + 1))
            else:
                dp[i][j] = min(dp[i - 1][k] + time_change for k in range(max(initial_speed, j) - time_change, min(final_speed, j) + time_change))

    return dp[time_change][final_speed]

if __name__ == "__main__":
    initial_speed, final_speed, time_change = map(int, input().split())
    print(max_distance(initial_speed, final_speed, time_change))
