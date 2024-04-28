def has_subset_sum_divisible_by_m(arr, m):
    memo = {0:True}

    def has_subset_sum_sum_j(divisible_sum_j):
        for x in arr:
            new_sum_j = x + divisible_sum_j
            if new_sum_j not in memo:
                memo[new_sum_j] = has_subset_sum_sum_j(new_sum_j) or (new_sum_j % m == 0)
            if memo[new_sum_j]:
                return True
        return False

    return has_subset_sum_sum_j(0)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(has_subset_sum_divisible_by_m(arr, m))
