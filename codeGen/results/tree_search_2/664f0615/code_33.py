from sys import stdin

def solve():
    init_speed, final_speed, time, max_change = map(int, stdin.readline().split())
    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]

    for t in range(1, time + 1):
        for s in range(1, final_speed + 1):
            if abs(s - init_speed) <= max_change:
                dp[t][s] = min(dp[t-1][init_speed] + (s - init_speed), dp[t-1][s])
            else:
                dp[t][s] = dp[t-1][s]

    return max(dp[-1])

print(solve())
