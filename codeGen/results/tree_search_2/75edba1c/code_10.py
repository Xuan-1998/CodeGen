def count_subarrays(N, K, Arr):
    dp = [[False for _ in range(N+1)] for _ in range(N+1)]

    max_val = max(Arr)
    for i in range(N-1, -1, -1):
        for j in range(i, N):
            if Arr[j] > K and (j == N-1 or Arr[j] > max_val):
                dp[i][j] = True
            elif Arr[j] <= K:
                dp[i][j] = False
            else:
                dp[i][j] = dp[i][j+1]

    res = 0
    for i in range(N-1, -1, -1):
        for j in range(i, N):
            if dp[i][j]:
                res += 1

    return res

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
