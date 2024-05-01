from typing import Tuple

def max_path_length(initial_speed: int, final_speed: int, time: int, max_allowed_change_in_speed: int) -> int:
    dp = [[[0] * (max_allowed_change_in_speed + 1) for _ in range(final_speed - initial_speed + 1)] for _ in range(time + 1)]

    for t in range(1, time + 1):
        for v in range(initial_speed, final_speed + 1):
            dp[t][v - initial_speed][max_allowed_change_in_speed] = max(dp[t-1][k][max_allowed_change_in_speed] + k for k in range(max(v - max_allowed_change_in_speed, initial_speed), min(v + max_allowed_change_in_speed, final_speed) + 1))
    return max(dp[time][v][max_allowed_change_in_speed] for v in range(initial_speed, final_speed + 1))

if __name__ == "__main__":
    initial_speed, final_speed, time, max_allowed_change_in_speed = map(int, input().split())
    print(max_path_length(initial_speed, final_speed, time, max_allowed_change_in_speed))
