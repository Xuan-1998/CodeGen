import sys

def count_subarrays(N, K, Arr):
    # Initialize dp array with all zeros
    dp = [0] * (N + 1)

    max_val = Arr[0]
    dp[0] = 1 if max_val > K else 0

    for i in range(1, N):
        if Arr[i] > K:
            dp[i] = dp[i - 1] + 1
        elif Arr[i] <= K and max(Arr[:i]) > K:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1]

    return sum(dp)

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
