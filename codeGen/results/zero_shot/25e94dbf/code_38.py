import sys

cmd = input().strip()
n = int(input())

max_dist = 0
dist = 0

for c in cmd:
    if c == 'F':
        dist += 1
    elif c == 'T':
        dist = 0
    max_dist = max(max_dist, dist)

# Modify commands to maximize distance
for i in range(n):
    new_cmd = list(cmd)
    for j in range(min(i+1, len(new_cmd))):
        if new_cmd[j] == 'F':
            new_cmd[j] = 'T'
        elif new_cmd[j] == 'T':
            new_cmd[j] = 'F'
    for c in new_cmd:
        if c == 'F':
            dist += 1
        elif c == 'T':
            dist = 0
        max_dist = max(max_dist, dist)

print(max_dist)
