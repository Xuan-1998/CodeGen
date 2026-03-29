import sys

def min_operations_to_increasing_order():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i][j] = min(dp[i][j], dp[j][i-1] + 1)
    
    return max(max(row) for row in dp)

print(min_operations_to_increasing_order())
