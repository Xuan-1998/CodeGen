from collections import deque

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if i < k:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][k - j] + (s[i - k] != s[i - k + 1]))
    
    ans = min(dp[n - k][k], dp[n - k][n % k])
    print(ans)

if __name__ == "__main__":
    solve()
