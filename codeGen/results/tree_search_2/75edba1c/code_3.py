import sys

def count_subarrays(N, K, Arr):
    max_seen = max(Arr)
    dp = [0]*N
    if max_seen > K:
        dp[0] = 1
    for i in range(1, N):
        if Arr[i] > K and max_seen > K:
            dp[i] = dp[i-1] + 1
        elif Arr[i] > K and max_seen <= K:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1]
    return sum(dp)

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
