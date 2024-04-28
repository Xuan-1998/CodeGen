def solve():
    init_speed, final_speed, time, max_diff = [int(x) for x in input().split()]
    
    dp = [[0] * (max_diff + 1) for _ in range(time + 1)]
    prev_speeds = [init_speed]
    
    for i in range(1, time + 1):
        for diff in range(max_diff + 1):
            if i == 1:
                dp[i][diff] = min(prev_speeds[0], final_speed) * i
            else:
                for prev_diff in range(max_diff + 1):
                    if abs(prev_speeds[-1] - (prev_speeds[-1] + diff)) <= max_diff:
                        dp[i][diff] = max(dp[i][diff], dp[i-1][prev_diff] + min(prev_speeds[-1], final_speed) * i)
            prev_speeds.append(min(prev_speeds[-1], final_speed) + diff if abs(min(prev_speeds[-1], final_speed) - (min(prev_speeds[-1], final_speed) + diff)) <= max_diff else min(prev_speeds[-1], final_speed))
    
    return max(dp[-1])

print(solve())
