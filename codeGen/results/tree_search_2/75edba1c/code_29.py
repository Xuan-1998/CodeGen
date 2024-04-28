import sys

def count_subarrays(arr, K):
    N = len(arr)
    dp = {(i, k): 0 for i in range(N) for k in range(K+1)}

    # Base case: There are no subarrays of length 0 or negative.
    dp[0, k] = 0 for k in range(K+1)]

    for i in range(1, N):
        for k in range(K+1):
            if arr[i-1] > K:
                dp[i, k] = dp[i-1, k] + 1
            else:
                dp[i, k] = dp[i-1, k]

    result = 0
    for i in range(N):
        for k in range(K+1):
            if arr[i] > K:
                result += dp[i, k]
    return result

# Read input from stdin
N, K = map(int, input().split())
arr = list(map(int, input().split()))

print(count_subarrays(arr, K))
