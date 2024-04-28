def can_sum_divisible_by_m(n, m):
    dp = [False] * (m + 1)
    dp[0] = True

    for x in range(1, n + 1):
        for i in range(m, x - 1, -1):
            if dp[i - x]:
                dp[i] = True

    return any(dp[i] and i % m == 0 for i in range(m + 1))

n = int(input())
m = int(input())
set_ = list(map(int, input().split()))
print(can_sum_divisible_by_m(n, m))
