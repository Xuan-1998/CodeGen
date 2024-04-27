import sys
import math

def count_permutations(n):
    # Initialize the count of valid permutations
    count = 0
    
    # Iterate over all possible permutations of length n
    for permutation in itertools.permutations(range(1, n+1)):
        # Check if the first x elements of the permutation are sorted
        is_sorted = True
        for i in range(1, min(n, len(permutation))):
            if permutation[i] < permutation[i-1]:
                is_sorted = False
                break
        
        # If the permutation satisfies the condition, increment the count
        if is_sorted:
            count += 1
    
    return count

n = int(sys.stdin.readline())
print(count_permutations(n))
