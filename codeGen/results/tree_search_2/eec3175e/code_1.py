def can_subset_sum_divisible(arr, m):
    n = len(arr)
    dp = [False] * (n + 1)

    dp[0] = True

    for i in range(1, n + 1):
        if arr[i - 1] % m == 0:
            dp[i] = True
        else:
            dp[i] = any(dp[j] and (arr[i - 1] + sum(arr[:j])) % m == 0 for j in range(i))

    return dp[-1]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(can_subset_sum_divisible(arr, m))
