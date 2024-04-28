from collections import defaultdict

def max_path_length():
    initial_speed, final_speed = map(int, input().split())
    time, max_change = map(int, input().split())

    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]

    for i in range(1, time + 1):
        for j in range(1, final_speed + 1):
            if i == 1:
                dp[i][j] = min(j - initial_speed, abs(final_speed - j))
            else:
                dp[i][j] = max(dp[i-1][k] + k - (j-1) for k in range(max(0, j-max_change), min(final_speed+1, j+max_change)+1))

    return dp[time][final_speed]

print(max_path_length())
