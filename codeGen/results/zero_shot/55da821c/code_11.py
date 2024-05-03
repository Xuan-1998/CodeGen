import sys

n, m = map(int, input().split())
plants = []

for _ in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((int(s), float(x)))

plants.sort(key=lambda x: x[1])

replantings = 0

for i in range(1, m):
    current_species = None
    for _, x in plants:
        if int(x) > (10**9) / m * (i - 1):
            break
        species = int(_)
        if species != current_species and current_species is not None:
            replantings += 1
        current_species = species

replantings += len(plants) - m

print(replantings)
