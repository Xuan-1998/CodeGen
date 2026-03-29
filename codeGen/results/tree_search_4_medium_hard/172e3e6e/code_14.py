MOD = 10**9 + 7

def solve(n, a):
    dp = [0] * (n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        for j in range(i):
            if a[i] % (j+1) == 0:
                dp[i] += dp[j]
        dp[i] %= MOD
    
    return dp[n]

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
