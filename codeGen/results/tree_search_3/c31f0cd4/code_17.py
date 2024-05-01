def find_distinct_sums(N, A):
    # Initialize an empty set to store unique sums found so far
    distinct_sums = set()
    
    # Generate all possible subsets using bit manipulation
    for i in range(1 << N):  # 2^N is the number of subsets
        subset_sum = 0
        for j in range(N):
            if (i & (1 << j)):
                subset_sum += A[j]
        
        # Add the sum to the set, but only if it's not already present
        distinct_sums.add(subset_sum)
    
    # Sort and return the unique sums as a list
    return sorted(list(distinct_sums))

# Read input from stdin
N = int(input())
A = [int(x) for x in input().split()]

print(' '.join(map(str, find_distinct_sums(N, A))))
