import sys

def max_distance(speed1, speed2, time, delta):
    dp = [[0] * (speed2 + 1) for _ in range(time + 1)]
    
    for j in range(speed1, speed2 + 1):
        if j == speed1:
            dp[1][j] = 1
        else:
            dp[1][j] = min(delta, 1)
        
        for i in range(2, time + 1):
            if j == speed2:
                dp[i][j] = max(dp[i-1][j], (i - 1) * j)
            else:
                dp[i][j] = max(dp[i-1][j], min(delta, i) + dp[i-1][min(j-delta, 0)+1])
    
    return max(dp[-1])

# Example usage
speed1, speed2, time, delta = map(int, input().split())
print(max_distance(speed1, speed2, time, delta))
