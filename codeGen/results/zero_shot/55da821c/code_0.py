python
n, m = map(int, input().split())
plants = []
for _ in range(n):
    species, x = map(float, input().split())
    plants.append((int(species), float(x)))

plants.sort(key=lambda x: x[1])

min_replant = 0
current_section = 0

for plant in plants:
    if plant[0] == current_section + 1:
        current_section += 1
    else:
        min_replant += 1
        current_section = plant[0]

print(min_replant)
