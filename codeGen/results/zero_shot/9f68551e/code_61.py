import sys

def solve():
    n = int(sys.stdin.readline())
    times = list(map(int, sys.stdin.readline().split()))
    healths = list(map(int, sys.stdin.readline().split()))

    times.sort()
    healths.sort()

    mana = 0
    prev_damage = 0

    for i in range(n):
        while times[i] > 1 and prev_damage < healths[i]:
            prev_damage += 1
        mana += prev_damage + 1
        prev_damage = max(prev_damage, healths[i])

    print(mana)

solve()
