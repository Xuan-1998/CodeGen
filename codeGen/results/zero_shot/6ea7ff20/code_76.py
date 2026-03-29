import sys

def merge(a, b):
    if not a:  # a is empty
        return b
    if not b:  # b is empty
        return a
    if a[0] < b[0]:  # a_1 < b_1
        return [a[0]] + merge(a[1:], b)
    else:  # a_1 > b_1
        return [b[0]] + merge(a, b[1:])

def solve(n, p):
    for i in range(n):
        if p[i] < p[n+i]:
            return "YES"
    return "NO"

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
print(solve(n, p))
