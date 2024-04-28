def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = max(dp[i-1], dp[max(0, i - 2)] if a[i-1] % 2 == 0 else dp[max(0, i - 1)], 
                    dp[min(n, i + 1)] if a[i-1] % 2 != 0 else dp[min(n, i)])
    
    print(dp[n])
