def can_sum_divisible_by_m(n, m, nums):
    dp = {0: True}
    total = 0
    for num in nums:
        total += num
        if total % m not in dp:
            dp[total % m] = False
        else:
            dp[total % m] = True
    return dp.get(total % m, False)

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
print(can_sum_divisible_by_m(n, m, nums))
