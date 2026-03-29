import sys

def max_score():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = arr[i - 1]
        for j in range(1, k + 1):
            for i in range(j, n + 1):
                if i <= z:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + arr[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + arr[i - 1], dp[i - z][j - 1] + arr[i - 1])
        print(dp[n][k])

if __name__ == "__main__":
    max_score()
