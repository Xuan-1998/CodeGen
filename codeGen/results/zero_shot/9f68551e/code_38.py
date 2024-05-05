import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))

k.sort()

max_health = max(h)

mana_required = [max_health - i + 1 for i in range(max_health)]

total_mana = sum(mana_required)
print(total_mana)
