def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = {0: 0}  # base case: dp[0] = 0 since there are no operations when x = 0
    
    for i in range(1, n):
        dp[i] = (a[i-1] + dp.get(i-1, 0)) % (n+1) if a[i-1] <= i else (a[i-1] - 1)
    
    return dp[n-1]

print(solve())
