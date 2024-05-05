import sys

def read_input():
    n = int(sys.stdin.readline())
    k = list(map(int, sys.stdin.readline().split()))
    h = list(map(int, sys.stdin.readline().split()))
    return n, k, h

n, k, h = read_input()
k.sort()

def calculate_mana_required(k, h):
    mana_required = 0
    for i in range(len(k)):
        max_damage = k[i] - (k[i] // h[i]) * h[i]
        mana_required += max_damage + (1 if i > 0 else 0)
    return mana_required

mana_required = calculate_mana_required(k, h)
print(mana_required)
