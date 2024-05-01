def solve():
    N = int(input())
    str1, str2 = input().split(), input().split()
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    print(dp[N-1][N-1])

if __name__ == "__main__":
    solve()
