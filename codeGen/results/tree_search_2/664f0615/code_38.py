from typing import Tuple

def solve() -> int:
    initial_speed, final_speed = map(int, input().split())
    travel_time, max_allowed_speed_change = map(int, input().split())

    dp: list[Tuple[int, ...]] = [[(0, 0)] * (travel_time + 1) for _ in range(final_speed + 1)]

    for time in range(travel_time + 1):
        for speed in range(initial_speed, final_speed + 1):
            if speed == initial_speed:
                dp[speed][time] = (speed, 0)
            elif time > 0 and abs(speed - dp[dp[speed][time-1]][0]) <= max_allowed_speed_change:
                dp[speed][time] = (speed, min(dp[speed][time-1][1] + speed, travel_time * speed))
            else:
                dp[speed][time] = (speed, 0)

    return max(max(row) for row in dp)
