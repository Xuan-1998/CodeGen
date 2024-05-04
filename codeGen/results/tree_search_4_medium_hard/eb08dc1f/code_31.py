def solve():
    n = int(input())
    dp = [[[0] * (n+1) for _ in range((10**n)-1)] for _ in range(n+1)]

    for j in range(1, n+1):
        for i in range(j-1, (10**j)-1):
            for k in range(i-j+1):
                dp[j][i][k] = sum(dp[min(k+1, d)][i-(10**k)] for d in range(min(k+1, 10))) + 1

    print(sum(dp[n][(10**n)-1][j] for j in range(n)) % 998244353)

solve()
