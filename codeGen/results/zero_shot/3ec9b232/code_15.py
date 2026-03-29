import sys

def solve():
    n = int(input())
    m = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Base case: merging 0 arrays
    for i in range(1, n + 1):
        dp[i][0] = 1

    # Fill up the dp table
    for j in range(1, n):
        for i in range(j + 1, n + 1):
            dp[i][j] = (dp[i - 1][j - 1] * (i - 1)) % (10**9 + 7)

    # Calculate the result
    res = dp[n][-1]
    print(res)

if __name__ == "__main__":
    solve()
