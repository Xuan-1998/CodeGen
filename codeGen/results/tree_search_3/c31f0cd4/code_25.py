def find_distinct_sums(nums):
    # Initialize the dictionary to store distinct sums
    dp = {0: [0]}

    for num in nums:
        # Generate all possible subsets using the current integer as the base
        for i, subset_sum in list(dp.items()):
            new_subsets = [subset + [num] for subset in dp.get(i, [])]
            for new_subset_sum in (sum(subset) for subset in new_subsets):
                if new_subset_sum not in dp:
                    dp[new_subset_sum] = []
                dp[new_subset_sum].extend(new_subset_sum - num + subset_sum)
                dp[new_subset_sum].sort()

    return ' '.join(str(sum) for sum in sorted(dp.keys()))

# Example usage
input_nums = [1, 2, 3]
print(find_distinct_sums(input_nums))
