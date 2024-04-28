def max_partitions(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(n - 1, -1, -1):
        right_sum = total_sum - left_sum
        if arr[i] == (left_sum - right_sum):
            dp[i][i] = dp[i + 1][n - 1] + 1
        else:
            dp[i][i] = max(dp[i + 1][n - 1], 1)
        
        left_sum += arr[i]
    
    return dp[0][n - 1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
