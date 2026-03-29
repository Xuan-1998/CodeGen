import sys

def solve():
    t = input().strip()
    n = int(input())
    s = [input() for _ in range(n)]

    m = 0
    for i, si in enumerate(s):
        pos = 0
        while True:
            pos = t.find(si, pos)
            if pos == -1:
                break
            m += 1
            print(f"{i+1} {pos}")

    if m == 0:
        print(-1)
    else:
        print(m)

if __name__ == "__main__":
    solve()
