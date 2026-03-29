import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    dp = [[0.0 for _ in range(n+1)] for _ in range(m+1)]

    # Calculate base cases
    for k in range(n+1):
        if k >= s[h-1]:
            dp[0][k] = 1.0
        else:
            dp[0][k] = 0.0

    # Fill up the dp array
    for i in range(1, m+1):
        for j in range(n, -1, -1):
            if s[i-1] >= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-n+i])
            else:
                dp[i][j] = dp[i-1][j]

    # Return the answer
    print(max(0.0, 1.0 - dp[m-1][n]))

if __name__ == "__main__":
    solve()
