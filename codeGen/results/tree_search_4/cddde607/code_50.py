def count_paths_to_collect_k_coins(K, N, arr):
    dp = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]

    # Base case: there's only one way to reach the top-left cell (i.e., you're starting from that point)
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(N):
            for k in range(K+1):
                if i < N-1:
                    dp[i][j][k] += dp[i+1][j][min(k, arr[i][j])]
                if j < N-1:
                    dp[i][j][k] += dp[i][j+1][min(k, arr[i][j])]

    return dp[N-1][N-1][K]

# Example usage:
K = int(input())  # number of coins to collect
N = int(input())  # size of the matrix
arr = [[int(x) for x in input().split()] for _ in range(N)]

print(count_paths_to_collect_k_coins(K, N, arr))
