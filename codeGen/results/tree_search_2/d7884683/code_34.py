import sys

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        
        for j in range(i):
            if left_sum == right_sum:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] + 1)
            else:
                dp[i][j] = dp[i-1][j]
    
    print(max(dp[n]))

solve()
