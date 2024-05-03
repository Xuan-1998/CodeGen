n, m = map(int, input().split())
species_positions = [0] * (m + 1)
for _ in range(n):
    s, x = map(float, input().split())
    species_positions[s] += x

replanted = 0
for i in range(1, m):
    diff = species_positions[i] - species_positions[i-1]
    if diff > 0:
        replanted += diff
        for j in range(i, m):
            species_positions[j] -= diff

print(replanted)
