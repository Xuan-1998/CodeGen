from itertools import chain, combinations

def find_distinct_sums(nums):
    # Initialize an empty set to store unique sums
    distinct_sums = set()

    # Generate all possible subsets of the input list
    for r in range(len(nums) + 1):
        subsets = chain(*map(lambda x: combinations(nums, x), range(r+1)))
        
        # Iterate over each subset and calculate its sum
        for subset in subsets:
            subset_sum = sum(subset)
            
            # Add the sum to our set of distinct sums
            if subset_sum not in distinct_sums:
                distinct_sums.add(subset_sum)

    return sorted(list(distinct_sums))

# Example usage:
N = int(input())
nums = [int(x) for x in input().split()]
print(' '.join(map(str, find_distinct_sums(nums))))
