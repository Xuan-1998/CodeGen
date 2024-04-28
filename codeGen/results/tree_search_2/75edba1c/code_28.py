def count_subarrays(N, K, Arr):
    memo = {}
    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        if i == N - 1:
            return 0
        res = 0
        max_val = max(Arr[i:])
        if max_val > K:
            res += 1
        for j in range(i + 1, N):
            if Arr[j] > K:
                res += 1
        memo[(i, k)] = res
        return res

    res = 0
    for i in range(N - 1):
        max_val = max(Arr[i:])
        res += dp(i, max_val)

    return res

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
