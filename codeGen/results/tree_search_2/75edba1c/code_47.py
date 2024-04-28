def count_subarrays(K):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * (n + 1)

    memo = {}

    for i in range(n):
        if arr[i] > K:
            prev_max = max(memo.get(i-1, 0), arr[i])
            dp[i+1] = dp[i] + (prev_max > K)
            memo[i] = prev_max
        else:
            dp[i+1] = dp[i]

    return sum(dp) - dp[0]
