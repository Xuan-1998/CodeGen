import sys

def coin_paths(K, N, arr):
    # Initialize DP table with zeros
    dp = [[0] * (N) for _ in range(N)]

    def dfs(i, j, k):
        if i == N - 1 and j == N - 1:
            return 1 if k == K else 0
        if k > K or i < 0 or j < 0:
            return 0

        if dp[i][j]:
            return dp[i][j]

        result = 0
        if i + 1 < N and arr[i+1][j] <= K - k:
            result += dfs(i + 1, j, k + arr[i][j])
        if j + 1 < N and arr[i][j+1] <= K - k:
            result += dfs(i, j + 1, k + arr[i][j])

        dp[i][j] = result
        return result

    # Main function to count paths
    return dfs(0, 0, 0)

if __name__ == "__main__":
    K, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(coin_paths(K, N, arr))
