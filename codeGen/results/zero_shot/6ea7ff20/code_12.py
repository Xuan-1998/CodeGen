import sys

def merge(a, b):
    result = []
    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result.extend(a or b)
    return result

def check_permutation(p):
    n = len(p) // 2
    a, b = [], []
    for pi in p:
        if not a or pi < a[0]:
            a.append(pi)
        else:
            b.append(pi)
    return set(a).isdisjoint(set(b))

n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]
if check_permutation(p):
    print("YES")
else:
    print("NO")
