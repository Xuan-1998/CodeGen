def distinct_sums(nums):
    memo = {}  # Initialize a hashmap for memoization

    def dfs(subset_sum, subset):
        if (subset_sum,) in memo:
            return memo[(subset_sum,)]
        
        total_sums = set()
        
        if len(subset) == 0:  # Base case: empty set
            total_sums.add(0)
        else:
            first_element = subset[0]
            remaining_subset = subset[1:]
            
            for subset_sum in dfs(subset_sum - first_element, remaining_subset):
                total_sums.add(subset_sum + first_element)
            
            total_sums.add(subset_sum)  # Add the sum of the current subset
            
        memo[(subset_sum,)] = total_sums
        return total_sums
    
    nums.sort()  # Ensure consistent ordering for subsets

    distinct_sums_set = dfs(sum(nums), nums)

    return ' '.join(map(str, sorted(distinct_sums_set)))
