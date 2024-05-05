import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    k = list(map(int, sys.stdin.readline().split()))
    h = list(map(int, sys.stdin.readline().split()))

    k.sort()

    mana = []
    for i in range(n):
        max_damage = 0
        for j in range(i, n):
            if k[j] - k[i] >= h[j]:
                max_damage = max(max_damage, k[j] - k[i])
        mana.append(max_damage)

    total_mana = sum(mana)
    print(total_mana)
