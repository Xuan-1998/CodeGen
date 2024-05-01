from itertools import chain, combinations
from collections import defaultdict

def find_sums(nums):
    # Generate all subsets and their corresponding sums
    subset_sums = {}
    for r in range(1, len(nums) + 1):
        for subset in combinations(nums, r):
            total_sum = sum(subset)
            if total_sum not in subset_sums:
                subset_sums[total_sum] = set()
            subset_sums[total_sum].add(frozenset(subset))

    # Initialize the dynamic programming table
    memo = defaultdict(int)

    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums) + 1):
            total_sum = sum(chain(*combinations(nums[:i], j - i), [num]))
            if total_sum not in memo:
                memo[total_sum] = set()
            memo[total_sum].add(frozenset(combinations(nums[:i], j - i)) | {frozenset([num])})

    # Generate the final list of distinct sums
    result = sorted(set(memo.values()).popitem()[1])
    return ' '.join(map(str, result))
