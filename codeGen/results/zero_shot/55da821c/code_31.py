import sys

n, m = map(int, sys.stdin.readline().split())
plants = {}

for i in range(n):
    s_i, x_i = map(float, sys.stdin.readline().split())
    if s_i not in plants:
        plants[s_i] = []
    plants[s_i].append(x_i)

for s in range(1, m+1):
    plants[s].sort()

replantings = 0

for s in range(1, m+1):
    prev_x = -float('inf')
    for x in plants[s]:
        if x > prev_x:
            replantings += 1
        prev_x = x

print(replantings)
