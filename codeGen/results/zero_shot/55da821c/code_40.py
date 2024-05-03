n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

replanted = 0
sections = {}
for s, x in plants:
    if s not in sections:
        sections[s] = []
    sections[s].append(x)

for s, pos in sections.items():
    for i in range(1, len(pos)):
        if pos[i-1] > pos[i]:
            replanted += 1

print(replanted)
