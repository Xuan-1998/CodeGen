import itertools
from collections import defaultdict

def generate_distinct_sums():
    N = int(input())
    nums = list(map(int, input().split()))
    
    # Initialize a dictionary to keep track of the encountered sums
    sum_dict = defaultdict(bool)
    
    # Generate all possible subsets of the given set
    for r in range(N + 1):
        for subset in itertools.combinations(nums, r):
            # Compute the sum of the current subset
            subset_sum = sum(subset)
            
            # Update the dictionary based on whether or not the sum has been encountered before
            sum_dict[subset_sum] = True

    # Generate a sorted list of distinct sums and print it out
    distinct_sums = [sum for sum in sorted(sum_dict) if sum_dict[sum]]
    
    return ' '.join(map(str, distinct_sums))

print(generate_distinct_sums())
