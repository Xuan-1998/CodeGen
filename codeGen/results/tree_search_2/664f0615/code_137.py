import sys

def solve():
    init_speed, final_speed = map(int, input().split())
    time, max_delta = map(int, input().split())

    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]

    for t in range(1, time + 1):
        for s in range(min(final_speed, init_speed), -1, -1):
            if s <= init_speed:
                dp[t][s] = max(dp[t-1][s], s * (t-1))
            elif s > init_speed and t >= 2:
                dp[t][s] = max(dp[t-1][s], dp[t-2][init_speed] + (s-init_speed) * (t-2))

    return max([dp[time][s] for s in range(init_speed, final_speed+1)])

if __name__ == '__main__':
    print(solve())
