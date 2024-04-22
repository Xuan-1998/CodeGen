MOD = 1000000007

def count_sequences(sets):
    # Initialize the dp array with the number of elements in the first set
    dp = len(sets[0])
    total_ways = dp  # Total ways without considering previous set
    
    for i in range(1, len(sets)):
        current_set = sets[i]
        prev_set = sets[i-1]
        
        # Count common elements
        common_elements = len(set(current_set).intersection(set(prev_set)))
        
        # Calculate number of ways to end with a non-common element
        ways_with_non_common = (total_ways - common_elements) * len(current_set) % MOD
        
        # Calculate number of ways to end with a common element
        ways_with_common = common_elements * (len(current_set) - 1) % MOD
        
        # Update the total number of ways for the current set
        dp = (ways_with_non_common + ways_with_common) % MOD
        
        # Update the total_ways for the next iteration
        total_ways = len(current_set)
    
    return dp

# Read input
N = int(input().strip())
sets = [list(map(int, input().strip().split()))[1:] for _ in range(N)]

# Calculate and print the result
print(count_sequences(sets))