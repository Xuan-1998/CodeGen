import sys

def merge(a, b):
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result.extend(a)
    result.extend(b)
    return result

def check_permutation(p):
    n = len(p) // 2
    a = p[:n]
    b = p[n:]
    for x in a:
        if x in b:
            return "NO"
    return "YES"

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    print(check_permutation(p))
