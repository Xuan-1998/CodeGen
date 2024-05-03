n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))
plants.sort(key=lambda x: x[1])
section_boundaries = [0] * m
for s, x in plants:
    idx = s - 1
    section_boundaries[idx] = max(section_boundaries[idx], x)
replant_cost = 0
for i in range(1, m):
    replant_cost += section_boundaries[i] - section_boundaries[i-1]
print(replant_cost)
