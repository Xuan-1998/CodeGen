def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, n + 1):
            dp[0][i] = i
        for j in range(1, m + 1):
            for k in range(n, 0, -1):
                if k > 9:
                    dp[j][k] = min(dp[j-1][k//10] + 2, k)
                else:
                    dp[j][k] = k
        print(dp[m][n] % (10**9 + 7))

if __name__ == "__main__":
    solve()
