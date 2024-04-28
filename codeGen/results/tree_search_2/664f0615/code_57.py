import sys

def read_input():
    return map(int, raw_input().split()), map(int, raw_input().split())

def max_length(initial_speed, final_speed, time, max_change):
    dp = [[0 for _ in range(time + 1)] for _ in range(final_speed - initial_speed + 1)]
    
    for speed_diff in range(final_speed - initial_speed + 1):
        if speed_diff <= 0:
            dp[speed_diff][0] = 0
        else:
            for t in range(1, time + 1):
                if speed_diff <= max_change and (t == 1 or dp[speed_diff][t-1] > 0):
                    dp[speed_diff][t] = min(dp[speed_diff][t-1], dp[min(speed_diff+max_change, final_speed - initial_speed)][t-1]) + 1
                else:
                    dp[speed_diff][t] = dp[speed_diff][t-1]
    
    return max(dp[-1])

initial_speed, final_speed = read_input()
time, max_change = read_input()

print(max_length(initial_speed, final_speed, time, max_change))
