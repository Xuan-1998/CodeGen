def partition_counts():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + arr[i]
        
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(i):
                if prefix_sum[i] - prefix_sum[j] == prefix_sum[j]:
                    dp[i][j] = max(dp[i-1][k] + 1 for k in range(j)) or 0
                else:
                    dp[i][j] = dp[i-1][j]
        
        print(max(max(row) for row in dp))

partition_counts()
