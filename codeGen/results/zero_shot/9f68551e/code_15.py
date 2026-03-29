import sys

def solve():
    n = int(sys.stdin.readline())
    monsters = []
    for _ in range(n):
        k, h = map(int, sys.stdin.readline().split())
        monsters.append((k, h))
    monsters.sort(key=lambda x: x[0])

    mana_required = 0
    prev_damage = 1
    for k, h in monsters:
        damage = max(h, prev_damage + 1)
        mana_required += damage
        prev_damage = damage

    print(mana_required)

if __name__ == "__main__":
    solve()
