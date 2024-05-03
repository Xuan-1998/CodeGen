n = int(input())
m = int(input())
plants = []
for _ in range(n):
    s, x = map(int, input().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

replants = 0
for i in range(1, n):
    if plants[i][0] != plants[i-1][0]:
        replants += 1

print(replants)
