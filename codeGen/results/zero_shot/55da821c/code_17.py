import sys

def min_replantings():
    n, m = map(int, input().split())
    plants = []
    for _ in range(n):
        s, x = map(float, input().split())
        plants.append((s, x))

    plants.sort(key=lambda x: x[1])

    species_plants = {}
    for s, x in plants:
        if s not in species_plants:
            species_plants[s] = []
        species_plants[s].append(x)

    replantings = 0
    for i in range(1, m):
        replantings += sum(species_plants[i][j-1] - species_plants[i-1][-1] for j in range(len(species_plants[i])) if species_plants[i-1])

    print(replantings)

min_replantings()
