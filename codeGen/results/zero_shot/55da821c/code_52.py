n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))
plants.sort(key=lambda x: x[1])

borders = [plants[0][1]]
for i in range(1, m):
    for j in range(i, n):
        if plants[j][0] == i + 1:
            borders.append(plants[j][1])
            break

replantations = 0
for i in range(m):
    start, end = borders[i-1], borders[i]
    for j in range(start, end+1):
        if plants[j][0] != i + 1:
            replantations += 1

print(replantations)
