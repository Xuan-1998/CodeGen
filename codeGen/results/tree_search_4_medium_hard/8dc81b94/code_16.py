import sys

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[False] * (sum(arr) + 1) for _ in range(n + 1)]
    
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(sum(arr) + 1):
            if j >= arr[i - 1]:
                dp[i][j] = (dp[i][j] or dp[i - 1][j - arr[i - 1]])
            if dp[i - 1][j]:
                dp[i][j] = True
    
    print("YES" if dp[n][0] else "NO")

solve()
