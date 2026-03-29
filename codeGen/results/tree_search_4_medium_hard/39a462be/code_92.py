import sys

def solve():
    A = input().strip()
    B = input().strip()

    n = len(A)
    m = len(B)

    dp = [[[0] * (k + 1) for k in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(min(i, j) + 1):
                if A[i - k] == B[j - k]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i - 1][j - 1][k])

    score = 0
    for k in range(min(n, m) + 1):
        score = max(score, dp[n][m][k] * 4 - (n + m))

    print(score)

if __name__ == '__main__':
    solve()
