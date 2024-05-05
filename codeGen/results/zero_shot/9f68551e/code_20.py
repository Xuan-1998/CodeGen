import sys

def min_mana_required(monsters):
    n = len(monsters)
    sorted_monsters = sorted((k, h) for k, h in monsters)
    mana = 0
    prev_damage = 0
    for k, h in sorted_monsters:
        while mana < h:
            mana += 1
        mana += max(0, prev_damage - (h - 1))
        prev_damage = max(mana, prev_damage + 1)
    return mana

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        monsters = []
        for _ in range(n):
            k, h = map(int, sys.stdin.readline().split())
            monsters.append((k, h))
        print(min_mana_required(monsters))

if __name__ == '__main__':
    main()
