import sys

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    return [b[0]] + merge(a, b[1:])

def check_permutation(p):
    n = len(p) // 2
    for i in range(len(p)):
        a = p[:i+1]
        b = p[i+1:]
        if sorted(a) == sorted(b):
            return "YES"
    return "NO"

# Read input from stdin
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

# Check permutation and print result to stdout
print(check_permutation(p))
