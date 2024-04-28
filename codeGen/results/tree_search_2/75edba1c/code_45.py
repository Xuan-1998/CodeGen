def count_subarrays(Arr, K):
    N = len(Arr)
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        max_val = max(Arr[:i])
        if max_val > K:
            dp[i][max_val] = dp[i - 1][max_val]
            if i < N and Arr[i] > max_val:
                dp[i][max_val] += 1
    return sum(sum(dp) for dp in dp)

# Read input from standard input
N, K = map(int, input().split())
Arr = list(map(int, input().split()))

print(count_subarrays(Arr, K))
