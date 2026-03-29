import sys

def solve():
    n, q = map(int, input().split())
    signs = input()

    dp = [[0] * (n + 1) for _ in range(q + 1)]

    for i in range(1, q + 1):
        l_i, r_i = map(int, input().split())

        for j in range(l_i - 1, r_i):
            if signs[j] == '+':
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[0][j - 1])

    for i in range(1, q + 1):
        print(min(dp[i]))

if __name__ == "__main__":
    solve()
