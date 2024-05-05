def solve():
    n = int(input())
    s = input()
    
    dp = [[[0] * (1 << 20) for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            for k in range(2**20):
                if ((k & (1 << (i-j-1))) and s[i:j+1]):
                    dp[i][j][k] = max(dp[i][j-1][k], dp[i-1][j][k])
    
    k = 0
    for i in range(n):
        for j in range(i, n):
            if (dp[i][j][k]):
                print(bin(k)[2:].zfill(n))
                return

solve()
