import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))

k.sort()

mana_required = 0

for i in range(n):
    while k[i] > mana_required + 1:
        mana_required += 1
    mana_required = max(mana_required, h[i])

total_mana_required = mana_required

print(total_mana_required)
