def max_partitions():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(1, n + 1):
            left_sum += arr[i - 1]
            
            for j in range(i, -1, -1):
                if left_sum == (total_sum - left_sum):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        print(max(map(max, dp)))

max_partitions()
