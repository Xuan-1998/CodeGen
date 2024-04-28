from collections import defaultdict

def max_partitions():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        total_sum = sum(arr)
        
        dp = [[0] * (total_sum + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, total_sum + 1):
                if arr[i - 1] == j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i - 1]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]
        
        print(max(j for i in range(n, -1, -1) for j in range(total_sum // 2, -1, -1) if dp[i][j] == (n - i)))
