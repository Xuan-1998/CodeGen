def numPathsWithKCoins(N, K, arr):
    dp = [[False] * N for _ in range(N)]
    dp[0][0] = True

    for i in range(N):
        for j in range(N):
            if i > 0 and dp[i-1][j]:
                remaining_coins = K - arr[i-1][j]
                if remaining_coins >= 0:
                    dp[i][j] = True
            if j > 0 and dp[i][j-1]:
                remaining_coins = K - arr[i][j-1]
                if remaining_coins >= 0:
                    dp[i][j] = True

    return dp[N-1][N-1]

if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(numPathsWithKCoins(N, K, arr))
