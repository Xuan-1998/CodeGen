import sys

def min_replanting():
    n, m = map(int, input().split())
    plants = []
    for _ in range(n):
        s, x = map(float, input().split())
        plants.append((int(s), x))

    # Sort plants by species and then by position
    plants.sort(key=lambda p: (p[0], p[1]))

    # Initialize the replanting count to 0
    replants = 0

    # Iterate through the sorted plants
    for i in range(1, m):
        # If a plant is out of place, increment the replanting count
        if plants[i-1][1] > plants[i][1]:
            replants += 1

    print(replants)

min_replanting()
