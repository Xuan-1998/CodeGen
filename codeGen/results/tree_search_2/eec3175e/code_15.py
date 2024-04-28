def find_subset_sum_divisible(set, m):
    memo = {}
    for num in set:
        remaining_sum = (num % m)
        if remaining_sum not in memo:
            memo[remaining_sum] = True
        else:
            memo[remaining_sum] = False

    for num in set:
        new_remaining_sum = (num + sum(set[:set.index(num)])) % m
        if new_remaining_sum not in memo or not memo[new_remaining_sum]:
            return 1
    return 0

n, m = map(int, input().split())
set = list(map(int, input().split()))
print(find_subset_sum_divisible(set, m))
