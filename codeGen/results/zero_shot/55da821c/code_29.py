n, m = map(int, input().split())
plants = []
for _ in range(n):
    species, position = map(float, input().split())
    plants.append((int(species), int(position)))
desired_permutation = [i for i in range(1, m+1)]

plants.sort(key=lambda x: x[1])
replanted = 0
for i, (species, _) in enumerate(plants):
    if species != desired_permutation[i]:
        replanted += 1
print(replanted)
