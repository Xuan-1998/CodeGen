import sys

def solve():
    q = int(sys.stdin.readline())
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        found = False
        for j in range(2**30):
            if (u & j) == j and ((j & v) == v):
                found = True
                break
        if found:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
