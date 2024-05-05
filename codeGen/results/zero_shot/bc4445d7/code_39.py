import math

def calculate_distribution_index(n, edges):
    # Initialize the distribution index to 0
    distribution_index = 0
    
    # Iterate over all pairs of nodes (i, j)
    for i in range(1, n):
        for j in range(i+1, n):
            # Calculate the distribution index for edge (i, j)
            f_ij = math.prod(range(n-2, -1, -1)) + 1
            
            # Add it to the total distribution index
            distribution_index += f_ij
    
    return distribution_index % (10**9 + 7)

# Read input from stdin
n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]
m = int(input())
prime_factors = list(map(int, input().split()))

# Calculate the distribution index and print it to stdout
print(calculate_distribution_index(n, edges))
