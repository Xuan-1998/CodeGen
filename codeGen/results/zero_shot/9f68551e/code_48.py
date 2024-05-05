import sys

def solve():
    n = int(sys.stdin.readline())
    monsters = []
    for _ in range(n):
        k, h = map(int, sys.stdin.readline().split())
        monsters.append((k, h))

    monsters.sort()

    min_mana = 0
    for i, (k, h) in enumerate(monsters):
        max_damage = k - i
        min_mana = max(min_mana, max_damage)

    print(min_mana)

if __name__ == "__main__":
    solve()
