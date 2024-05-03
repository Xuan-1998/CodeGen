n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

left = []
right = []
last_species = None

for i, (s, _) in enumerate(plants):
    if s != last_species:
        left.append(i)
    right.append(i)
    last_species = s

replant_count = sum(1 for i in range(len(left) - 1))

print(replant_count)
