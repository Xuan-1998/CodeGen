import math

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (k + 1) for _ in range(k + 1)]
        dp[0][0] = 1
        for i in range(1, k + 1):
            for j in range(i, -1, -1):
                if j >= i:
                    dp[i][j] += dp[i-1][j-i] * 2
                else:
                    dp[i][j] = dp[i-1][j]
        res = 0
        for j in range(k + 1):
            res += dp[k][j]
        print(res % (10**9 + 7))

if __name__ == "__main__":
    solve()
