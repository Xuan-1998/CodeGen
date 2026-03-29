import sys; input = lambda:sys.stdin.readline().strip(); MOD = 10**9 + 7

def solve():
    n = int(input())
    m = list(map(int, input().split()))
    dp = [[0]*(1<<n) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for p in range((1<<i)-1, -1, -1):
            if (p & (1<<(m[i-1]-1))) == 0:
                dp[i][p] += dp[i-1][p]
            else:
                for j in range(i):
                    if ((p >> j) & 1) and m[j] < m[i-1]:
                        dp[i][p] += dp[j][p ^ (1<<j)]
    print(dp[n][(1<<n)-1]%MOD)

solve()
