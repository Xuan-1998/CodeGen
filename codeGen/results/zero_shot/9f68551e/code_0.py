import sys

n = int(sys.stdin.readline())
total_mana = 0
for _ in range(n):
    k, h = map(int, sys.stdin.readline().split())
    total_mana += max(1, k - (k - h)) + sum(range(k - h))
print(total_mana)
