def count_subarrays(N, K, Arr):
    memo = {}

    def dp(i, k):
        if (i, k) not in memo:
            if i >= N or Arr[i] > k:
                result = 1 if i == N-1 else 0
            else:
                result = dp(i+1, k)
                if Arr[i] <= k:
                    result += 1
            memo[(i, k)] = result
        return memo[(i, k)]

    total_count = 0
    for i in range(N):
        total_count += dp(i, K)

    return total_count

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
