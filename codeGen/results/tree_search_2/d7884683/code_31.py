from collections import defaultdict

def partition_array():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Initialize dp table with default value 0
        dp = [[0] * (n // 2 + 1) for _ in range(n + 1)]
        
        total_sum = sum(arr)
        
        for i in range(1, n + 1):
            left_sum = 0
            for j in range(i - 1, -1, -1):
                left_sum += arr[j]
                if left_sum == (total_sum - left_sum) // 2:
                    dp[i][j] = 1 + ((dp[j-1][j//2-1] + dp[i-j-1][(n-i)//2-1]) if j > 0 and i > j else 0)
        
        print(max(map(max, dp)))

partition_array()
