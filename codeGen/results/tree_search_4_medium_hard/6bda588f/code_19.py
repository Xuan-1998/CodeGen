import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        total = 0
        for ai in map(int, sys.stdin.readline().split()):
            if ai > s:
                total += (ai - s) * (s)
            elif ai < s:
                total += (s - ai) * (s)
            else:
                total += ai * (s)
        print(total)

if __name__ == "__main__":
    solve()
