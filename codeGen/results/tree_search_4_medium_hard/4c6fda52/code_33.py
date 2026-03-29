def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (k+1) for _ in range(n+1)]

    # Initialize base cases
    for j in range(k):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(min(i, k)):
            if s[i-1] == s[(i+j)%3]:  # %3 because 'RGB' has a cycle of length 3
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][k-j-1])

    print(dp[n-1][k-1])

if __name__ == "__main__":
    for _ in range(int(input())):  # Read number of queries
        solve()
