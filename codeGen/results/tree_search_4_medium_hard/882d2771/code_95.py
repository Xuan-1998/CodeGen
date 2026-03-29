code
def solve():
    t, l, r = map(int, input().split())
    
    MOD = 10**9 + 7
    
    dp = [[0] * (r - l + 1) for _ in range(r + 1)]
    
    for i in range(1, r + 1):
        if i == 1:
            dp[i][0] = 1
        else:
            for j in range(1, i):
                if j >= l:
                    dp[i][j - l] = (dp[j][j - l - 1] * (i - 1) + 1) % MOD
                else:
                    dp[i][j] = (dp[j][0] * (i - 1) + 1) % MOD
    
    res = 0
    for i in range(l, r + 1):
        if i == l:
            res += t * (1 - l)
        else:
            res += t * dp[i][r - i]
    
    print(res % MOD)

if __name__ == "__main__":
    solve()
