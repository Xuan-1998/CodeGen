from sys import stdin

def calculate_length():
    initial_speed, final_speed, time, max_change = [int(x) for x in stdin.readline().split()]
    dp = [[[0]*(max(initial_speed, final_speed)+1) for _ in range(max(initial_speed, final_speed)+1)] for _ in range(time+1)]

    for i in range(1, time+1):
        for speed in range(min(initial_speed, final_speed), max(initial_speed, final_speed)+1):
            for prev_speed in range(min(initial_speed, final_speed), max(initial_speed, final_speed)+1):
                if abs(speed-prev_speed) <= max_change:
                    dp[i][speed][prev_speed] = min(dp[i-1][speed-1][prev_speed], dp[i-1][speed+1][prev_speed]) + 1

    return max(max([max(dp[i][speed][prev_speed] for speed in range(min(initial_speed, final_speed), max(initial_speed, final_speed)+1)) for prev_speed in range(min(initial_speed, final_speed), max(initial_speed, final_speed)+1))) for i in range(time+1))

print(calculate_length())
