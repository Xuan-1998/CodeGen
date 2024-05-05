import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        p = list(map(int, sys.stdin.readline().split()))
        a = set()
        b = set()
        for i in range(n):
            if p[i] < p[n+i]:
                a.add(p[i])
                b.add(p[n+i])
            else:
                b.add(p[i])
                a.add(p[n+i])
        if len(a) + len(b) == 2*n and not a & b:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
