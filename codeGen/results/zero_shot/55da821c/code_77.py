n, m = map(int, input().split())
plants = []
for _ in range(n):
    species, x = map(float, input().split())
    plants.append((species, x))

replanted = 0
sections = [[] for _ in range(m)]
for i in range(m):
    sections[i].append((i+1, 0))  # initialize with a dummy plant at position 0

plants.sort(key=lambda x: x[1])

for plant in plants:
    species, x = plant
    for i in range(m):
        if not sections[i] or sections[i][-1][1] <= x:
            sections[species-1].append(plant)
            break

replanted = sum(len(section) - len(set(section)) for section in sections)

print(replanted)
