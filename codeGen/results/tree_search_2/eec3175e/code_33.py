n = int(input())  # number of integers in the set
m = int(input())  # value to check divisibility by
integers = [int(x) for x in input().split()]  # the set of integers

result = can_sum_divisible(n, m, integers)
print(result)  # output: 1 if a subset sum is divisible by m, 0 otherwise
