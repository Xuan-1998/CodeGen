def count_subarrays(N, K, Arr):
    dp = [[0] * (K + 1) for _ in range(N)]

    for i in range(N):
        max_val = max(Arr[:i+1])
        for j in range(K, max_val, -1):
            if max_val > j:
                dp[i][j] = 1
                break

    res = 0
    for i in range(N-1):
        for j in range(K + 1):
            if dp[i][j]:
                res += 1
            dp[i+1][j] = max(dp[i][j], dp[i][max(Arr[:i+1])])

    return res

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
