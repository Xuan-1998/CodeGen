import sys

def merge(a, b):
    if not a:  # a is empty
        return b
    elif not b:  # b is empty
        return a
    elif a[0] < b[0]:  # a's first element is smaller than b's first element
        return [a[0]] + merge(a[1:], b)
    else:  # b's first element is smaller than or equal to a's first element
        return [b[0]] + merge(a, b[1:])

def solve(n):
    p = list(map(int, sys.stdin.readline().split()))
    for i in range(2*n):
        if p[i] > p[i+1]:
            a = p[:i+1]
            b = p[i+1:]
            break
    else:
        return "NO"
    if len(a) != n or len(b) != n:
        return "NO"
    for x in a:
        if x in b:
            return "NO"
    return "YES"

n = int(sys.stdin.readline())
for _ in range(n):
    print(solve(int(sys.stdin.readline())))
