from sys import stdin

def calculate_path_segment_length():
    initial_speed, final_speed = map(int, stdin.readline().split())
    time, max_speed_change = map(int, stdin.readline().split())

    dp = [[0] * (time + 1) for _ in range(final_speed - initial_speed + 1)]
    dp[0][0] = 0

    for i in range(1, final_speed - initial_speed + 1):
        for j in range(min(i, time), -1, -1):
            if i == 0:
                break
            if j >= 1 and abs(initial_speed + i - dp[i-1][j-1]) <= max_speed_change:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + (initial_speed + i) * j)
            else:
                break

    return dp[final_speed - initial_speed][time]

print(calculate_path_segment_length())
