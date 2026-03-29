def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def check_permutation(p):
    n = len(p) // 2
    for i in range(n):
        if p[i] > p[n+i]:
            break
    else:
        return "YES"
    for j in range(i+1, n+i):
        if p[j] < p[j-i-1]:
            break
    else:
        return "NO"
    return "YES"

import sys

n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]
print(check_permutation(p))
