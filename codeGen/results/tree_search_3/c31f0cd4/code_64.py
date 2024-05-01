from itertools import chain

def find_distinct_sums():
    N = int(input())
    nums = [int(x) for x in input().split()]
    
    cumulative_sums = set()
    
    for i in range(1, N+1):
        cum_sum = 0
        for j in range(i):
            cum_sum += nums[j]
            
            # Add the current subset's sum to our set of distinct sums
            cumulative_sums.add(cum_sum)
        
        # Add this new element's value to all existing subsets
        for cum_sum in list(cumulative_sums):
            cumulative_sums.add(cum_sum + nums[i-1])
    
    return sorted(list(cumulative_sums))

print(" ".join(map(str, find_distinct_sums())))
