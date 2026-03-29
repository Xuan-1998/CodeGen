import sys

def merge(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()

for i in range(1, len(p)):
    if p[i] == p[i-1]:
        print("NO")
        sys.exit()

if len(p) % 2 != 0:
    print("NO")
    sys.exit()

i = 0
while i < len(p):
    j = i + 1
    while j < len(p) and p[j] <= p[i]:
        j += 1
    a.append(p[i])
    b = p[i+1:j]
    if merge(a, b) == p:
        print("YES")
        sys.exit()
    i = j

print("NO")
