import sys

def solve():
    initial_speed, final_speed, time, max_change = [int(x) for x in input().split()]
    
    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]
    
    for i in range(1, time + 1):
        for j in range(initial_speed, final_speed + 1):
            if i == 1:
                dp[i][j] = min(j - initial_speed, final_speed - j)
            else:
                dp[i][j] = max(dp[i-1][max(0, j-max_change)], dp[i-1][min(final_speed, j+max_change)])
    
    return dp[-1][-1]

print(solve())
