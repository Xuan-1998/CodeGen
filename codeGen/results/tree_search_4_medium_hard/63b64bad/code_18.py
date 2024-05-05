from collections import defaultdict

def get_final_values():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [[[defaultdict(int) for _ in range(10)] for _ in range(n+1)] for _ in range(n+1)]
    cumulative_sum = [0]
    current_value = 0

    for i in range(n):
        cumulative_sum.append(cumulative_sum[i] + a[i])
    
    for x in range(1, n+1):
        for y in range(cumulative_sum[x-1]):
            state = (x, y, cumulative_sum[x-1], current_value)
            dp[x][y][state[2]] = state
            
            next_x = min(x + a[x-1], n) if x + a[x-1] <= n else 0
            next_y = y + a[x-1]
            
            while (next_x, next_y, cumulative_sum[next_x-1], current_value) in dp[next_x][next_y][state[2]]:
                next_x -= a[next_x-1]
                next_y += a[next_x-1]
            
            if (next_x, next_y, cumulative_sum[next_x-1], current_value) == (0, 0, cumulative_sum[-2], 0):
                dp[x][y][state[2]][(0, 0, cumulative_sum[-2], 0)] = -1
            else:
                dp[x][y][state[2]][(next_x, next_y, cumulative_sum[next_x-1], current_value)] = state
            
    for i in range(n):
        print(dp[i][cumulative_sum[i]-1][i][0])
