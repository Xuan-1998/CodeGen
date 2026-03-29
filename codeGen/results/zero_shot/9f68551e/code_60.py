import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        k = list(map(int, sys.stdin.readline().split()))
        h = list(map(int, sys.stdin.readline().split()))

        mana = 0
        for i in range(n-1, -1, -1):
            mana += max(1, h[i] - (k[i+1] - k[i]))

        print(mana)

if __name__ == '__main__':
    solve()
