import sys

n, m = map(int, input().split())  
plants = []  

for _ in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((int(s), float(x)))

plants.sort(key=lambda x: x[1])

replantings = 0
for i in range(m):
    section_start = None
    for plant in plants:
        if plant[1] <= section_start or section_start is None:
            if i > 0:  
                replantings += 1
            section_start = plant[1]
        else:
            break

print(replantings)
