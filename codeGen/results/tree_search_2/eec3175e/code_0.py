def can_subset_sum_divisible_by_m(n, m, nums):
    total_sum = sum(nums)
    dp = [False] * (total_sum // m + 1)

    for num in nums:
        for i in range(total_sum // m, num - 1, -1):
            if not dp[i - num]:
                dp[i] = True

    return any(dp)


# Example usage:
n = int(input())  # number of elements
m = int(input())  # value to check divisibility with
nums = [int(x) for x in input().split()]  # array of non-negative integers

print(can_subset_sum_divisible_by_m(n, m, nums))
