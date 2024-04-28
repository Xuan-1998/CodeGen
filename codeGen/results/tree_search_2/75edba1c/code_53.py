def count_subarrays(arr, K):
    N = len(arr)
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    memo = {}

    def dp_helper(i, prev_max):
        if (i, prev_max) in memo:
            return memo[(i, prev_max)]

        if i == 0:
            return 0

        curr_max = max(arr[:i+1])
        if curr_max > K:
            result = 1 + dp_helper(i-1, curr_max)
        else:
            result = dp_helper(i-1, prev_max)

        memo[(i, prev_max)] = result
        return result

    for i in range(N):
        prev_max = max(arr[:i+1])
        for j in range(K+1):
            if prev_max > j:
                dp[i][j] = 1 + dp_helper(i-1, prev_max)
            else:
                dp[i][j] = dp[i-1][j]

    return sum(dp[-1])

# Example usage
N, K = map(int, input().split())
arr = list(map(int, input().split()))
print(count_subarrays(arr, K))
