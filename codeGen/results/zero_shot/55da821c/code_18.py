import sys

n, m = map(int, input().split())
plants = []

for _ in range(n):
    species, x = map(float, input().split())
    plants.append((species, x))

plants.sort(key=lambda x: x[1])

ans = 0
last_section = -1

for plant in plants:
    if plant[0] > last_section + 1:
        ans += m - last_section - 1
        last_section = plant[0]
    else:
        last_section = plant[0]

print(ans)
