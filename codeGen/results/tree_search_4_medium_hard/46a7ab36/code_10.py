import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (n // 2 + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, m + 1):
            for j in range(n // 2 + 1):
                if i == 1:
                    dp[i][j] = n - 1
                else:
                    for k in range(i - 1):
                        p = min(j, (n + 1) // 2)
                        dp[i][j] += dp[k][p]
        print(dp[m][0] % (10**8 + 7))

if __name__ == "__main__":
    solve()
