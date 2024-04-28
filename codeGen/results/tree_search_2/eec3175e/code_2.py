def can_sum_divisible(m, nums):
    n = len(nums)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        if i % m == 0:
            dp[i] = True
        else:
            for j in range(i):
                if dp[j] and (i - j) % m == 0:
                    dp[i] = True
                    break

    return dp[n]

m, n = map(int, input().split())
nums = list(map(int, input().split()))
print(can_sum_divisible(m, nums))
