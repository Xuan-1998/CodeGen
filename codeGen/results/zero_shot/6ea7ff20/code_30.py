import sys

def merge(a, b):
    result = []
    while a and b:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result.extend(a)
    result.extend(b)
    return result

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

a = []
b = []

for num in p:
    if len(a) < n and not any(x == num for x in a):
        a.append(num)
    elif len(b) < n and not any(x == num for x in b):
        b.append(num)

if len(a) + len(b) == 2*n and set(a).isdisjoint(set(b)):
    print("YES")
else:
    print("NO")
