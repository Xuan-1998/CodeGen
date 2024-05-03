import sys

def min_replants(n, m):
    # Initialize an array to store the species and positions of plants
    plants = [[s, x] for s, x in zip([int(x) for x in sys.stdin.readline().split()], [float(x) for x in sys.stdin.read().split()])]

    # Sort the plants by their positions
    plants.sort(key=lambda x: x[1])

    # Initialize variables to store the minimum number of replants and the current species
    min_replants = 0
    curr_species = None

    # Iterate through the sorted plants
    for s, x in plants:
        if s != curr_species:
            # If we've encountered a different species, increment the count of replants
            min_replants += 1
            curr_species = s

    return min_replants

# Read input and print output
n, m = map(int, sys.stdin.readline().split())
print(min_replants(n, m))
