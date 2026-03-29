import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    # Create dp array and initialize it with infinity
    dp = [[sys.maxsize] * (k + 1) for _ in range(n + 1)]

    # Base case: if j == 0, then we don't need to make any changes
    for i in range(n + 1):
        dp[i][0] = 0

    # Fill up the dp array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, min(i + 1, k) + 1):
            if s[i - 1] != 'RGB'[j % 3]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i - 1][j]

    # The answer is the minimum number of changes needed to make the substring s[0..n-1] equal to a substring of 'RGBRGBRGB...'
    print(dp[n - 1][k - 1])

if __name__ == "__main__":
    solve()
