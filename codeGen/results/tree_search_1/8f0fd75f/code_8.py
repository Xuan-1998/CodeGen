import sys

def find_min_durability(n, coords, durability):
    max_span = [(durability[i], i) for i in range(n)]  # (max span, index)
    
    # Initialize max_span based on the initial durability and distances
    for i in range(n):
        left_dist = coords[i+1] - coords[i]
        right_dist = coords[i+2] - coords[i+1]
        max_span[i] = (min(durability[i], left_dist, right_dist), i)
    
    # Sort points by their max_span
    max_span.sort()
    
    # Redistribute the load as points collapse
    for span, i in max_span:
        if i > 0:  # Update the left neighbor
            left_idx = i - 1
            left_dist = coords[i+1] - coords[left_idx+1]
            durability[left_idx] -= left_dist
            if durability[left_idx] < 0:
                return -durability[left_idx]  # Additional durability needed
        
        if i < n - 1:  # Update the right neighbor
            right_idx = i + 1
            right_dist = coords[right_idx+1] - coords[i+1]
            durability[right_idx] -= right_dist
            if durability[right_idx] < 0:
                return -durability[right_idx]  # Additional durability needed
    
    return 0  # No additional durability needed if we reach here

# Read input from stdin
n = int(sys.stdin.readline())
coords = list(map(int, sys.stdin.readline().split()))
durability = list(map(int, sys.stdin.readline().split()))

# Find and print the result
print(find_min_durability(n, coords, durability))
