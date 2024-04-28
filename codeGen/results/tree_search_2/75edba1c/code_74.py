def count_subarrays(Arr, K):
    N = len(Arr)
    dp = [0] * N

    for i in range(N):
        max_in_range = max(Arr[i-N:i+1])
        if max_in_range > K:
            dp[i] = i + 1
        else:
            prev_subarrays = sum(dp[j-1] for j in range(i) if max(Arr[j:i+1]) > K)
            dp[i] = prev_subarrays

    return sum(1 for x in dp if x > 0)

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(Arr, K))
