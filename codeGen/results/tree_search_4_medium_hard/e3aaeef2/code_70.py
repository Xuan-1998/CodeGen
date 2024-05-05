import sys

def solve():
    t = int(input())
    mod = 10**9 + 7
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = i

    for j in range(1, m+1):
        for i in range(j, n+1):
            dp[i][j] = max(dp[i-1][j-1], i)

    print(sum([dp[i][m] % mod for i in range(n+1)]))

if __name__ == "__main__":
    solve()
