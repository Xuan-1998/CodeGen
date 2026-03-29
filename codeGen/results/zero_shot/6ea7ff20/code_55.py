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

def is_mergeable(p):
    n = len(p) // 2
    left, right = p[:n], p[n:]
    if any(x in y for x in zip(left, right)):
        return False
    return True

while True:
    try:
        n = int(sys.stdin.readline())
        p = list(map(int, sys.stdin.readline().split()))
        if is_mergeable(p):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
