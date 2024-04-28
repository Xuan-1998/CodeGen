def is_divisible_by_m(nums, m):
    memo = {0: True}
    total_sum = 0

    for num in nums:
        total_sum += num
        remainder = total_sum % m
        if remainder not in memo:
            memo[remainder] = any((i % m == 0) or (memo.get(i, False)) for i in range(1, remainder + 1))
        print(memo)
    return memo.get(total_sum % m, False)

n = int(input())
m = int(input())
nums = [int(x) for x in input().split()]
print(is_divisible_by_m(nums, m))
