def max_partitions():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        
        dp = [[0] * (n // 2 + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(min(i, n // 2) + 1):
                if prefix_sum[i] - prefix_sum[j] == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] + 1)
        print(max(dp[n]))

max_partitions()
