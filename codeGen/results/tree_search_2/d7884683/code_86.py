import sys

def max_partition(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        left_sum = sum(arr[:i])
        for j in range(i, -1, -1):
            right_sum = sum(arr[j:])
            if left_sum == right_sum:
                dp[i][j] = max(dp[i-1][j-1], 1) if i > 1 and j < n else 1
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] + dp[i][j-1])
    
    return max(max(row) for row in dp)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partition(arr))
