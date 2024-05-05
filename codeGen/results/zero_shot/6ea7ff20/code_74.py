import sys

def read_input():
    n = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().split()))
    return n, p

def merge(a, b):
    result = []
    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result.extend(a)
    result.extend(b)
    return result

n, p = read_input()
a = []
b = []

for i in range(len(p)):
    if all(x > p[i] for x in a) and all(x > p[i] for x in b):
        a.append(p[i])
    else:
        b.append(p[i])

if sorted(a) + sorted(b) == p:
    print("YES")
else:
    print("NO")
