def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [["" for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0:
                dp[i][j] = ""
            elif j < i:
                dp[i][j] = dp[i-1][j]
            else:
                if s[i-1] <= s[0]:
                    dp[i][j] = dp[i-1][j-1] + s[i-1]
                else:
                    dp[i][j] = dp[i-1][j]

    print(dp[n][k])

if __name__ == "__main__":
    solve()
