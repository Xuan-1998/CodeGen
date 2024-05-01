def num_paths_to_collect_k_coins(N, K, arr):
    memo = {}

    def dp(i, j, k):
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        if i > N - 1 or j > N - 1 or k < 0:
            return 0

        if i == N - 1 and j == N - 1:
            return 1 if k == arr[i][j] else 0

        memo[(i, j, k)] = dp(i + 1, j, min(k, arr[i][j])) + \
                            dp(i, j + 1, max(0, k - arr[i][j]))

        return memo[(i, j, k)]

    return dp(0, 0, K)
