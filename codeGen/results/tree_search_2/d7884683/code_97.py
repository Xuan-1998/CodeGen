import sys
from collections import defaultdict

def partition_array():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        
        dp = defaultdict(lambda: sys.maxsize)
        dp[0] = 0
        
        max_partitions = 0
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if prefix_sum[j] == prefix_sum[i] - prefix_sum[j]:
                    dp[i] = min(dp[i], dp[j] + 1)
            max_partitions = max(max_partitions, dp[i])
        
        print(max_partitions)

partition_array()
