import sys

n, m = map(int, sys.stdin.readline().split())
plants = []
for i in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

sections = []
for i in range(m):
    sections.append([i])

plants_in_section = [[] for _ in range(m)]

for s, x in plants:
    # Find the first plant that doesn't belong in its current section
    for j in range(m):
        if len(plant[j]) > 0 and plant[j][-1] == s:
            sections.append([j])
            break

    # Add the current plant to its corresponding section
    for j, sect in enumerate(sections):
        if sect[0] == s:
            plants_in_section[s].append(x)
            break

replanted_plants = 0
for i in range(m):
    if len(plants_in_section[i]) > 1:
        replanted_plants += sum([plants_in_section[i][j] - plants_in_section[i][0] for j in range(1, len(plants_in_section[i]))])

print(replanted_plants)
