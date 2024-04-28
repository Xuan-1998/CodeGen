from collections import defaultdict

def count_subarrays(N, K, Arr):
    dp = [0] * (N + 1)
    prev_maxes = defaultdict(int)

    for i in range(1, N + 1):
        if Arr[i - 1] > K:
            prev_maxes[Arr[i - 1]] += 1
        else:
            prev_maxes.clear()

        dp[i] = sum(prev_maxes.values())

    return dp[-1]
