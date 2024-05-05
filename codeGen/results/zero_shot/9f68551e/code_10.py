import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))

k.sort()

mana = 0

for i in range(n):
    max_damage = 0
    for j in range(i+1):
        if k[j] >= h[i]:
            max_damage = max(max_damage, j + 1)
    mana += max_damage

print(mana)
