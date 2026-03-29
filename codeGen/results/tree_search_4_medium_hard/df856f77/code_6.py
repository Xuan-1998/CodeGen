import sys

def min_operations():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] * (max(arr) + 1) for _ in range(n)]
    
    for i in range(1, n):
        prev_val = arr[i-1]
        for j in range(max(arr) + 1):
            if j >= prev_val:
                dp[i][j] = min(dp[i][j], dp[i-1][prev_val-1]) if prev_val > 1 else 0
            else:
                dp[i][j] = 1
    
    return max(0, sum([dp[i][arr[i]] for i in range(n)]))

print(min_operations())
