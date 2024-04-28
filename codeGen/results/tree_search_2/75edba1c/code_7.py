def count_subarrays(arr, K):
    N = len(arr)
    dp = [0] * N

    def max_element(subarray):
        return max(subarray)

    memo = {}

    for i in range(N):
        if arr[i] > K:
            dp[i] = 1
        else:
            dp[i] = sum(dp[:i-1]) + (1 if any(max_element(arr[:j+1]) > K for j in range(i)) else 0)

    return sum(dp)
