def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        a = list(map(int, input().split()))
        dp = [[0] * (z + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            if i <= z:
                dp[i][0] = max(0, dp[0][i - 1] + a[i])
            else:
                for j in range(min(i, z) + 1):
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[j])
        print(max(dp[k]))

if __name__ == "__main__":
    solve()
