import sys

def solve():
    A, B = [input() for _ in range(2)]
    n, m = len(A), len(B)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    similarity_score = 4 * dp[n][m] - (n + m)

    print(similarity_score)

if __name__ == "__main__":
    solve()
