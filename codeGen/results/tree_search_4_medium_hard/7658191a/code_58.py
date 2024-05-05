===BEGIN CODE===
def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        dp = [[[0] * (z+1) for _ in range(n)] for _ in range(k+1)]

        for i in range(1, k+1):
            for j in range(i+1, n):
                if i <= z:
                    dp[i][j][i] = max(dp[i-1][j-1][i-1] + arr[j-1], dp[i][j-1][i] + arr[j])

        print(max(dp[k][n-1]))

solve()
===END CODE===
