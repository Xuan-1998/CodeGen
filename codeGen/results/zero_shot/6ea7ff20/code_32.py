import sys

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    return [b[0]] + merge(a, b[1:])

n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]
arr = p[:n] + p[n:]

for i in range(len(arr)):
    a = arr[:i]
    b = arr[i:]
    if len(a) == n and len(b) == n:
        merged = merge(a, b)
        if merged == p:
            print("YES")
            sys.exit(0)

print("NO")
