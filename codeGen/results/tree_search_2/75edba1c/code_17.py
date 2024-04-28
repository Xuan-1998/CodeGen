def count_subarrays(N, K, Arr):
    dp = [0] * (N + 1)
    max_val = max(Arr)
    for i in range(1, N + 1):
        if Arr[i - 1] > K and max(Arr[i:i + 1]) > K:
            for j in range(i):
                if Arr[j] <= K or max(Arr[j:i + 1]) <= K:
                    break
            dp[i] = dp[j - 1] + (i - j)
    return sum(dp)

# Example usage:
N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
