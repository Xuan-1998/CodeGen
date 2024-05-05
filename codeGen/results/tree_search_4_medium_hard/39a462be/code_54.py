from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    A = input()
    B = input()

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill up the base case first
    for i in range(n + 1):
        for j in range(m + 1):
            if not A[i:] or not B[j:]:
                continue

            if A[i] == B[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Fill up the rest of the dp table using dynamic programming
    for i in range(n + 1):
        for j in range(m + 1):
            if A[i:] and B[j:]:
                if A[i] == B[j]:
                    dp[i][j] = max(
                        dp[i - 1][j - 1] + 4,
                        dp[i - 1][j] + m - j,
                        dp[i][j - 1] + n - i
                    )
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                continue

    print(max(0, dp[n][m]) * 4 - (n + m))

if __name__ == "__main__":
    solve()
