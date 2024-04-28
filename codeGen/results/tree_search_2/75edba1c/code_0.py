def count_subarrays(N, K, Arr):
    dp = [0]*N
    max_so_far = 0

    for i in range(N):
        if Arr[i] > K:
            if i == 0 or dp[i-1] == 0:
                max_so_far += 1
            else:
                max_so_far = max(max_so_far, dp[i-1])
        dp[i] = max_so_far

    return sum(1 for x in dp if x > 0)

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
