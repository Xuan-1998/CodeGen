import sys

def can_sum_divisible_by_m(n, m, arr):
    cum_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        cum_sum[i] = cum_sum[i - 1] + arr[i - 1]

    dp = {0: True}

    for i in range(1, n + 1):
        if cum_sum[i] % m == 0:
            dp[cum_sum[i]] = True

        for j in range(i):
            if (cum_sum[j] * (i - j) + cum_sum[i]) % m == 0 and dp.get(cum_sum[j], False):
                dp[cum_sum[i]] = True
                break

    return int(dp.get(0, False))

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(can_sum_divisible_by_m(n, m, arr))
