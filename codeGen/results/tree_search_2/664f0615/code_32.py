import sys

def max_path_length():
    initial_speed, final_speed, time, max_allowed_change = map(int, input().split())
    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]

    for i in range(1, time + 1):
        for j in range(initial_speed, final_speed + 1):
            if j == initial_speed:
                dp[i][j] = j
            elif j == final_speed:
                dp[i][j] = (i - 1) * j + (time - i) * final_speed
            else:
                for prev_speed in range(max(0, j - max_allowed_change), min(final_speed, j + max_allowed_change + 1)):
                    dp[i][j] = max(dp[i][j], dp[i-1][prev_speed] + j)

    return max(dp[-1])

print(max_path_length())
