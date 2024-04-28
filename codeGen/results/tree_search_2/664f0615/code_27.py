from collections import defaultdict

def max_path_segment(initial_speed, final_speed, time, max_change):
    # Initialize the DP table with base cases
    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]
    dp[0][initial_speed] = initial_speed
    
    # Fill up the DP table using bottom-up dynamic programming
    for i in range(1, time + 1):
        for speed in range(initial_speed, final_speed + 1):
            if abs(speed - initial_speed) > max_change:
                dp[i][speed] = 0
            else:
                dp[i][speed] = dp[i-1][min(max(final_speed, speed), speed+max_change)] + 1
    
    # Find the maximum possible length of path segment
    return max(dp[-1])

# Read inputs from standard input
initial_speed, final_speed, time, max_change = map(int, input().split())

print(max_path_segment(initial_speed, final_speed, time, max_change))
