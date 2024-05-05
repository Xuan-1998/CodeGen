import sys

def solve():
    t, l, r = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (1 << t) for _ in range(r + 1)]
    
    for i in range(l):
        dp[i][0] = 1
    
    for i in range(l, r + 1):
        for j in range(1 << t):
            if not (j & (1 << (i - l))):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][k ^ j] for k in range(1 << t))
    
    ans = sum((t - i) * dp[i][2**t - 1] for i in range(l, r + 1)) % MOD
    print(ans)

if __name__ == "__main__":
    solve()
