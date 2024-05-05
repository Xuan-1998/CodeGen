def merge(a, b):
    if not a:
        return b
    if not b:
        return a

    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def can_decompose(p):
    n = len(p) // 2
    a_idx = b_idx = 0

    for i in range(len(p)):
        if a_idx < n and p[i] <= p[a_idx]:
            a_idx += 1
        elif b_idx < n and p[i] >= p[b_idx]:
            b_idx += 1
        else:
            return False

    return True

def solve(p):
    n = len(p) // 2

    if not can_decompose(p):
        return "NO"
    else:
        return "YES"

import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        p = list(map(int, sys.stdin.readline().split()))
        print(solve(p))

if __name__ == "__main__":
    main()
