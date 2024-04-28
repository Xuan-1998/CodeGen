import sys

def solve():
    # Read input
    initial_speed, final_speed = map(int, input().split())
    time, max_speed_diff = map(int, input().split())

    # Create a 2D DP table
    dp = [[0] * (max_speed_diff + 1) for _ in range(time + 1)]

    # Base case: the first segment
    for speed_diff in range(max_speed_diff + 1):
        if speed_diff <= max_speed_diff and initial_speed_to_new_speed(speed_diff, initial_speed, final_speed) <= final_speed:
            dp[0][speed_diff] = 1
        else:
            dp[0][speed_diff] = 0

    # Fill up the DP table
    for second in range(1, time + 1):
        for speed_diff in range(max_speed_diff + 1):
            if speed_diff <= max_speed_diff and initial_speed_to_new_speed(speed_diff, initial_speed, final_speed) <= final_speed:
                dp[second][speed_diff] = min(dp[second - 1][speed_diff - (new_speed - initial_speed)] or 0, dp[second - 1][speed_diff] + 1)
            else:
                dp[second][speed_diff] = 0

    # Find the maximum length of path segment
    max_length = 0
    for speed_diff in range(max_speed_diff + 1):
        max_length = max(max_length, dp[time][speed_diff])

    print(max_length)

def initial_speed_to_new_speed(speed_diff, initial_speed, final_speed):
    return min(initial_speed + speed_diff, final_speed) if speed_diff <= max_speed_diff else final_speed

if __name__ == "__main__":
    solve()
