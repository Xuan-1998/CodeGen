import sys

def solve():
    t = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    s = [sys.stdin.readline().strip() for _ in range(n)]
    m = 0
    steps = []
    used = {}

    for string in s:
        if string in t:
            used[string] = True
            steps.append((len(steps) + 1, t.index(string)))
            t = t.replace(string, '', 1)
            m += 1

    print(m)

    for i, (w, p) in enumerate(steps):
        print(f"{w} {p}")

solve()
