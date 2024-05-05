def solve():
    t = int(input())
    MOD = 10**9 + 7
    dp = [[0] * (2*10**5+1) for _ in range(10**9+7)]
    
    for n in range(10**9+7):
        if n == 0:
            dp[n][0] = 1
        else:
            last_digit = n % 10
            for m in range(2*10**5+1):
                if m > 0:
                    dp[n][m] = sum(dp[(k*10 + last_digit)][m-1] for k in range(9))
                elif m == 0:
                    dp[n][m] = 1
    
    for _ in range(t):
        n, m = map(int, input().split())
        print(dp[n][m]%MOD)

if __name__ == "__main__":
    solve()
