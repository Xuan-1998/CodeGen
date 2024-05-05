import sys

# Constants
MOD = int(1e9) + 7

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(m+1):
                if i == 1:
                    dp[i][j] = min(j, 1)
                else:
                    dp[i][j] = min((dp[i-1][j-1] + 1) % MOD, i)
        print(dp[n][m])

if __name__ == "__main__":
    solve()
