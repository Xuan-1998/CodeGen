def find_paths(arr, K):
    N = len(arr)
    dp = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] <= K:
                if i == N-1 and j == N-1:
                    dp[i][j][K] = 1
                else:
                    dp[i][j][K] = (dp[i+1][j][K-arr[i][j]] + 
                                    dp[i][j+1][K-arr[i][j]]) > 0
            else:
                dp[i][j][K] = 0

    return sum([sum(row) for row in dp[-1]])

# Example usage
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(find_paths(arr, K))
