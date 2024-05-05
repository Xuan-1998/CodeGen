def min_changes():
    while True:
        n, k = map(int, input().split())
        s = input()

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                if s[i-1] == 'R' and s[i-j:i].count('R') % 2 == 0:
                    dp[i][j] = dp[i-1][j-1]
                elif s[i-1] != 'R':
                    if j > k:
                        dp[i][j] = dp[i-1][j-1] + k - j + 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1

        print(dp[n][k] + 1)

if __name__ == "__main__":
    min_changes()
