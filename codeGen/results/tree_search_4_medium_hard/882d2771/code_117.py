def solution():
    t, l, r = map(int, input().split())
    
    dp = [[[0] * (l + 1) for _ in range(l + 1)] for _ in range(t + 1)]
    
    for i in range(1, t + 1):
        for j in range(l, min(r, l) + 1):
            if i == 1:
                dp[i][j][0] = 0
            else:
                for k in range(min(j, r - l)):
                    dp[i][j][k + 1] = min(dp[i-1][min(k, j-1)][:]
                                         + dp[1][r-l-k][:]
                                         )
        
    res = sum([i * (dp[i][l][k+1]) for i in range(t)])
    
    print((res - l * (dp[t][l][r])) % (10**9 + 7))

if __name__ == "__main__":
    solution()
