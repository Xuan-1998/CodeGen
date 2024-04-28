import sys

def solve():
    n, k = map(int, input().split())
    dp = { (1, 1) : 1 }

    for i in range(2, n+1):
        dp[i] = {}
        for j in range(2, min(i, j)+1):
            if j % (i // k) == 0 and j % k == 0:
                dp[i][j] = dp.get((i // k, j // k), 0) + dp.get((i, k), 0)
            else:
                dp[i][j] = 0

    print(dp[n][k] % 1000000007)

if __name__ == "__main__":
    solve()
