def beautycontest(t, l, r):
    MOD = 10**9 + 7
    
    dp = {1: 0}
    for i in range(2, r+1):
        dp[i] = (i-1) * (dp[i-1] + 2*dp[i-2]) % MOD
    
    return sum(tj * dj for tj, dj in zip(map(int, input().split()), [dp[i] - l * dp[r] for i in range(l, r+1)])) % MOD

if __name__ == "__main__":
    t, l, r = map(int, input().split())
    print(beautycontest(t, l, r))
