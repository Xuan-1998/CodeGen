import sys

def solve(n, k):
    s = input().strip()
    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

    # Base case: when j > n or i > n
    for i in range(1, n+1):
        for j in range(k+1):
            if j >= k:
                dp[i][j] = s[:i]
            elif i == 1:
                dp[i][j] = [''] * j + [s[0]]
            else:
                if s[i-1] <= s[i-2]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = s[:i]

    # Print the result
    print(min(dp[n][k], key=lambda x: ''.join(x)))

if __name__ == "__main__":
    n, k = map(int, input().split())
    solve(n, k)
