import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))

k.sort()

min_mana = 10**9

for i in range(n):
    while k[i] > h[i]:
        min_mana = max(min_mana, k[i])
        k[i] -= 1

print(min_mana)
