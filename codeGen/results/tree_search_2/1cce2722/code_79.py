def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if a[i - 1] % 2 == 0:
            dp[i] = max(dp[i-1], dp[i-1] + a[i-1] - 2)
        else:
            dp[i] = dp[i-1]
    
    print(max(0, dp[-1]))

solve()
