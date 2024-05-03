import sys

n, m = map(int, input().split())
plants = []

for i in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))

count = 0
for plant in plants:
    s, x = plant
    if s != (x // (10**9) % m + 1):  # check if the plant should be moved to its corresponding section
        count += 1

print(count)
