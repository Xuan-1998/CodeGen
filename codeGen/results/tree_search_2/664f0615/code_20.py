from sys import stdin

def solve():
    initial_speed, final_speed, time, max_diff = map(int, stdin.readline().split())
    dp = [[0] * (max_diff+1) for _ in range(time+1)]
    
    for i in range(1, time+1):
        for j in range(max_diff+1):
            if abs(initial_speed - j) <= initial_speed and abs(final_speed - j) <= final_speed:
                dp[i][j] = min(i-1, max(0, dp[i-1][abs(j-(initial_speed-final_speed))]))
    
    return max(dp[-1])

print(solve())
