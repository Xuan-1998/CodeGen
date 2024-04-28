def count_subarrays(K):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * n

    for i in range(n):
        max_element = max(arr[i:])
        if max_element > K:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + (1 if max_element > K else 0)

    return sum(dp)
