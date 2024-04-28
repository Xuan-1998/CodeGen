from sys import stdin

def max_path_length():
    # Read input from stdin
    init_speed, final_speed, time, max_speed_diff = [int(x) for x in stdin.readline().split()]
    
    # Initialize dynamic programming table
    dp = [[0] * (time + 1) for _ in range(final_speed - init_speed + 1)]
    
    # Fill up the dynamic programming table
    for diff in range(final_speed - init_speed):
        for t in range(2, time + 1):
            if abs(diff) <= max_speed_diff:
                dp[diff][t] = min(dp[diff][t-1], dp[max(diff+init_speed-final_speed, 0)][t-1])
    
    # Find the maximum possible length of the path segment
    return sum(range(final_speed + 1)) - (final_speed - init_speed) * time - dp[-1][-1]

print(max_path_length())
