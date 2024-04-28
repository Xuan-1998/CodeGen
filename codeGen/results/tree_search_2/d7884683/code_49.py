import sys

def max_partitions():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        left_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            left_sum[i] = left_sum[i-1] + arr[i-1]
        
        right_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            right_sum[i] = right_sum[i+1] + arr[i]
        
        max_partitions = 0
        for j in range(1, n):
            for i in range(j, n):
                if left_sum[j-1] == right_sum[i]:
                    dp[i][j] = max(dp[i][j], dp[j-1][i-1] + 1)
                    max_partitions = max(max_partitions, dp[i][j])
        
        print(max_partitions)

max_partitions()
