import sys

def merge(a, b):
    result = []
    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    return result + (a or b)

def check_permutation(n, p):
    a = [x for x in p[:n]]
    b = [x for x in p[n:]]
    if len(set(a) & set(b)) > 0:  # Check if there are common elements
        return "NO"
    else:
        return "YES" if merge(a, b) == p else "NO"

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    p = list(map(int, sys.stdin.readline().split()))
    print(check_permutation(n, p))
