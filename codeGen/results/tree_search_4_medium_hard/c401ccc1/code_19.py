import sys

def and_op(u, v):
    return u & v

def count_and_ops(u, v):
    ops = 0
    while u != v:
        if (u & 1) == 0:
            ops += 1
            u >>= 1
        else:
            ops += 1
            u &= ~1
    return ops

def solve():
    q = int(sys.stdin.readline())
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        if count_and_ops(u, v) == -1:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    solve()
