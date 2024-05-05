import sys

def merge(a, b):
    result = []
    while a and b:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    return result + a + b

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

found = False
for i in range(len(p)):
    if p[i] > 0 and (i % 2 == 1 or not found):
        print("NO")
        found = True
        break

if not found:
    print("YES" if merge(range(1, n+1), range(n, 2*n+1)) == p else "NO")
