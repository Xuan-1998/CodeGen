def can_sum_divisible_by_m(n, m, arr):
    dp = [False] * (m + 1)
    dp[0] = True

    for num in arr:
        for i in range(m, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
                break

    return dp[m]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(can_sum_divisible_by_m(n, m, arr))
