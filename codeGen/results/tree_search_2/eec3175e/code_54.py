def has_divisible_subset(n, m, nums):
    # Initialize memoization dictionary
    memo = {0: True}

    for num in nums:
        new_sums = {}
        for s, divisible in memo.items():
            new_sum = s + num
            if new_sum % m == 0:
                new_divisible = True
            else:
                new_divisible = False

            # Store the result in the memoization dictionary
            new_sums[new_sum] = new_divisible

        # Update the memoization dictionary with the new sums
        memo.update(new_sums)

    # Return whether there exists a subset with sum divisible by m
    return any(memo.values())

# Example usage:
n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(has_divisible_subset(n, m, nums))
