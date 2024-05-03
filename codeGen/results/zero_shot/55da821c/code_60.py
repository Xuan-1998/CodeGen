import sys

def min_replant(n, m):
    # Read input from stdin
    for _ in range(m):
        _, x = map(int, next(sys.stdin).split())
    plants = sorted([(int(x), int(s)) for _ in range(n) for s, x in zip(*[line.split() for line in sys.stdin])])

    # Initialize the minimum number of replants
    min_replanted = 0

    # Group plants by species and calculate the minimum number of replants
    species_count = {}
    for i, (x, s) in enumerate(plants):
        if s not in species_count:
            species_count[s] = []
        species_count[s].append(x)
    for s, xs in species_count.items():
        min_replanted += len(xs) - 1

    return min_replanted

# Read the number of plants and species from stdin
n, m = map(int, sys.stdin.readline().split())

print(min_replant(n, m))
