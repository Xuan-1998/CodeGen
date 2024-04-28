def can_sum_divisible_by_m(n, m, arr):
    # Create a dictionary to store previously computed sums and their indices
    memo = {0: 0}

    for num in arr:
        new_sums = {}
        for prev_sum, index in list(memo.items()):
            new_sum = prev_sum + num
            if new_sum % m == 0:
                return True
            new_sums[new_sum] = index

        memo.update(new_sums)

    return False


# Test the function
n = int(input())  # Number of elements in the set
m = int(input())  # Value to check divisibility by
arr = list(map(int, input().split()))  # Array of non-negative integers

print(1 if can_sum_divisible_by_m(n, m, arr) else 0)
