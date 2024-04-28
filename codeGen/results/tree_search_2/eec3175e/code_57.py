def find_subset_sum_divisible_by_m(n, m, elements):
    dp = {0: True}  # base case: sum is 0, which is always divisible by m
    total_sum = 0

    for element in elements:
        new_dp = {}
        for prev_sum in dp:
            total_sum += element
            if total_sum % m == 0:
                new_dp[total_sum] = True
            else:
                new_dp[total_sum] = prev_sum + element >= m or dp.get(prev_sum + element, False)
        dp = new_dp

    return any(dp.get(total_sum, False) for total_sum in range(m))

# Example usage:
n = int(input())  # number of elements
m = int(input())  # the value to divide by
elements = list(map(int, input().split()))  # array of n non-negative integers

print(find_subset_sum_divisible_by_m(n, m, elements))
