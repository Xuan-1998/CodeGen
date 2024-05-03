n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((int(s), float(x)))

plants.sort(key=lambda x: x[1])

borders = []
sections = {i: [] for i in range(1, m+1)}

for s, x in plants:
    sections[s].append(x)

replantings = 0
for species, plants in sections.items():
    if len(plants) > 1:
        replantings += len(plants) - 1

print(replantings)
