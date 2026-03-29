import sys

def merge(a, b):
    result = []
    while a and b:
        if a[0] < b[0]:
            result.append(a.pop(0))
        elif a[0] > b[0]:
            result.append(b.pop(0))
        else:
            break
    return result + (a or b)

def solve(n, p):
    for i in range(0, len(p), 2):
        if p[i] > p[i+1]:
            return "NO"
    a = []
    b = []
    for i in range(len(p)):
        if i % 2 == 0:
            a.append(p[i])
        else:
            b.append(p[i])
    if merge(a, b) != list(p):
        return "NO"
    return "YES"

n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]
print(solve(n, p))
