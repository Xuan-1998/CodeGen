from sys import stdin

def solve():
    initial_speed, final_speed, time, allowed_speed_change = map(int, stdin.readline().split())
    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]

    for i in range(1, time + 1):
        for speed in range(initial_speed, final_speed + 1):
            if abs(speed - initial_speed) <= allowed_speed_change:
                dp[i][speed] = dp[i-1][initial_speed] + time
            else:
                dp[i][speed] = max(dp[i-1][speed+allowed_speed_change], 0) + time

    return max(dp[-1])

print(solve())
