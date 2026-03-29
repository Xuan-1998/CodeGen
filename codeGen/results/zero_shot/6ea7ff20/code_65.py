import sys

def merge(a, b):
    if not a:
        return b
    elif not b:
        return a
    elif a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def solve(n, p):
    a = []
    b = []
    for pi in p:
        if len(a) > 0 and pi < a[0]:
            return "NO"
        elif len(b) > 0 and pi > b[0]:
            return "NO"
        elif pi not in a + b:
            return "NO"
        elif len(a) < n:
            a.append(pi)
        else:
            b.append(pi)
    if len(a) + len(b) == 2 * n:
        return "YES"
    else:
        return "NO"

n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]
print(solve(n, p))
