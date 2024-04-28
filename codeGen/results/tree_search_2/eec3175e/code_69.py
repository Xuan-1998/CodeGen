def is_divisible_by_m(n, m):
    # Initialize a dictionary to store memoized values
    memo = {}

    def get_sum_subset(i, s):
        # If we've already computed this subset sum, return it
        if (i, s) in memo:
            return memo[(i, s)]

        # Base case: if i is out of bounds or the current sum is too large,
        # just return False (since the subset won't be divisible by m)
        if i >= n or s > m:
            return 0

        # Compute the sum with and without the current element
        s_with = get_sum_subset(i + 1, s + [n[i]])
        s_without = get_sum_subset(i + 1, [])

        # Store the memoized value and return it
        memo[(i, s)] = (s % m == 0) or max(s_with, s_without)
        return memo[(i, s)]

    # Initialize the maximum sum to negative infinity
    max_sum = float('-inf')

    # Iterate over all possible subsets
    for i in range(n):
        max_sum = max(max_sum, get_sum_subset(i, [n[i]]))

    return (max_sum % m == 0)
