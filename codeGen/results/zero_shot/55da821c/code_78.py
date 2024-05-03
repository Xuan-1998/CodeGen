import sys

n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((int(s), float(x)))

plants.sort(key=lambda x: x[1])

min_replantings = 0
current_section_species = plants[0][0]

for i in range(1, n):
    if plants[i][0] != current_section_species:
        min_replantings += 1
        current_section_species = plants[i][0]

print(min_replantings)
