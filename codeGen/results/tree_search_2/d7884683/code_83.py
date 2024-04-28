import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    
    dp = [[0] * (total_sum // 2 + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, total_sum // 2 + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i - 1]] + arr[i - 1])
                
    return total_sum // 2 - dp[n][total_sum // 2]

print(solve())
