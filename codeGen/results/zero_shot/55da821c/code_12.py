n, m = map(int, input().split())
plants = []
species_count = {i+1: 0 for i in range(m)}

for _ in range(n):
    s, x = map(int, input().split())
    plants.append(x)
    species_count[s] += 1

plants.sort()

replant_count = 0
for i in range(m):
    start = sum(1 for x in plants if x < i*m)
    end = sum(1 for x in plants if x >= i*m)
    replant_count += species_count[i+1] - (end-start)

print(replant_count)
