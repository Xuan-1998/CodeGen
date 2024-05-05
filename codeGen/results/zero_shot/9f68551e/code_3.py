import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))

total_mana = 0
max_health = 0

for i in range(n):
    while k[i] > max_health:
        total_mana += max_health + 1
        max_health += 1
    total_mana += h[i]
    max_health = h[i]

print(total_mana)
