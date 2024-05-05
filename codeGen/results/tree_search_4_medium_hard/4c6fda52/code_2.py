import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[sys.maxsize for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(min(i, k), -1, -1):
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(
                    1 + (s[j-1] != 'RGB'[i%3]) if j > 0 else 0,
                    dp[i-1][j]
                )

    print(dp[n][k])

if __name__ == "__main__":
    solve()
