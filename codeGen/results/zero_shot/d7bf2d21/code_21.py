import sys

def count_lis(arr):
    n = len(arr)
    dp = [[1] * (n+1) for _ in range(n+1)]
    
    max_length = 0
    result = 0
    
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if arr[j-1] > arr[i-1]:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 1
                
    for i in range(1, n+1):
        if dp[i][n] == max_length:
            result += 1
            
    return result

arr = list(map(int, input().split()))
print(count_lis(arr))
