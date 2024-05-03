n = int(input())
m = int(input())
plants = []
for i in range(n):
    x, s = map(int, input().split())
    plants.append((x, s))

plants.sort(key=lambda x: x[0])

current_section = None
replants_needed = 0

for plant in plants:
    if plant[1] != current_section:
        replants_needed += m - 1
        current_section = plant[1]
    else:
        pass

print(replants_needed)
