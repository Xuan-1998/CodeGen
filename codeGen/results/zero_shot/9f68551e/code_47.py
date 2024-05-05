import sys

n = int(sys.stdin.readline())
monster_times = list(map(int, sys.stdin.readline().split()))
monster_healths = list(map(int, sys.stdin.readline().split()))

monster_times.sort()

required_mana = 0

for i in range(n):
    if monster_healths[i] <= monster_times[i]:
        continue
    required_mana = max(required_mana, monster_healths[i])

print(required_mana)
