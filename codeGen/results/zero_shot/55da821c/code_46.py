import sys

def min_replant(n, m):
    # Read input from stdin
    n, m = map(int, sys.stdin.readline().split())
    plants = []
    for i in range(n):
        s, x = map(int, sys.stdin.readline().split())
        plants.append((s, x))

    # Sort plants by species and then position
    plants.sort(key=lambda p: (p[0], p[1]))

    # Initialize the minimum number of replantings
    min_replanted = 0

    # Iterate through the sorted plants
    for i in range(1, n):
        if plants[i][0] != plants[i-1][0]:
            # If we encounter a different species, increment the count
            min_replanted += 1

    return min_replanted

# Read input from stdin and print output to stdout
n, m = map(int, sys.stdin.readline().split())
print(min_replant(n, m))
