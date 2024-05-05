import sys
from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[[0] * 2 for _ in range(q+1)] for _ in range(n)]

    for i in range(n):
        for j in range(min(i+1, q)+1):
            if i == 0:
                if signs[i] == '+':
                    dp[i][j][0] = 1
                    dp[i][j][1] = -1
                else:
                    dp[i][j][0] = -1
                    dp[i][j][1] = 1
            else:
                if signs[i] == '+':
                    dp[i][j][0] = dp[i-1][j][0] + (dp[i-1][j][1] % 2)
                    dp[i][j][1] = -dp[i-1][j][1]
                else:
                    dp[i][j][0] = -dp[i-1][j][0] - (dp[i-1][j][1] % 2)
                    dp[i][j][1] = dp[i-1][j][1]

    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[r][q-1][0] - dp[l-1][q-1][0], n-l+1))

if __name__ == "__main__":
    solve()
