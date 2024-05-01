n = int(input())  # number of elements in the set
m = int(input())  # value to check divisibility by
nums = [int(x) for x in input().split()]  # array of non-negative integers

result = can_subset_sum_divisible_by_m(n, m, nums)
print(result)
