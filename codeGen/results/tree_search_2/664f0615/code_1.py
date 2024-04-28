def max_path_length():
    init_speed, final_speed, time, max_change = map(int, input().split())
    
    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]
    
    for i in range(1, time + 1):
        for j in range(min(i, final_speed), init_speed - 1, -1):
            dp[i][j] = min(dp[i-1][k] + max((i-0.5) * k, (i-1) * init_speed + (j-0.5)) 
                          for k in range(j-max_change, j+max_change+1))
    
    return dp[-1][-1]

print(max_path_length())
