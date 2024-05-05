def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(m):
            for j in range(min(i+1, n), 0, -1):
                dp[j] += dp[j-1]
            if m > i:
                dp[n%2] += dp[n%2 - 1]
        print(dp[m]%10**9+7)
