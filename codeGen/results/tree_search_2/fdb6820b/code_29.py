import sys

def solve():
    m, N = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [[0] * (N + 1) for _ in range(m + 1)]

    # base case: forming a sum of 0 using i elements
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, N + 1):
            if arr[i - 1] <= j:
                dp[i][j] = (dp[i][j - arr[i - 1]] + dp[i - 1][j]) % (10**9 + 7)
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[m][N])

if __name__ == "__main__":
    solve()
