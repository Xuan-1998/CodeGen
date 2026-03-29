import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if j <= k:
                dp[i][j] = min(dp[i-1][j-1] + (s[i-1] != 'RGB'[i%3]), dp[i-1][j])
            else:
                dp[i][j] = dp[i-k][k] + (s[i-k-1] != 'RGB'[i%3])

    print(dp[n-1][k])

if __name__ == "__main__":
    solve()
