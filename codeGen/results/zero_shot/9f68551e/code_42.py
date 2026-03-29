import sys

def solve():
    n = int(sys.stdin.readline())
    monsters = []
    for _ in range(n):
        k, h = map(int, sys.stdin.readline().split())
        monsters.append((k, h))

    mana = 0
    for k, h in monsters:
        while k > 1 and h > 0:
            mana += 1
            k -= 1
            h -= 1

    print(mana)

if __name__ == "__main__":
    solve()
