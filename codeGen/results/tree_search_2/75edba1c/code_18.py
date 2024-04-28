import sys

def count_subarrays(N, K, Arr):
    dp = [0] * N
    for i in range(N):
        max_element = max(Arr[:i+1])
        if max_element > K:
            dp[i] = sum(dp[j-1] for j in range(i) if Arr[j] > K and max(Arr[j:i+1]) > K)
    return sum(dp)

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
