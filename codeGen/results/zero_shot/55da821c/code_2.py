n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((int(s), float(x)))
plants.sort(key=lambda x: x[1])
sections = [[] for _ in range(m)]
for s, x in plants:
    sections[s - 1].append((s, x))
replant_cost = sum(len(sect) for sect in sections[1:])
print(replant_cost)
