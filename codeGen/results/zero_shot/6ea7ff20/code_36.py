def merge(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    return [b[0]] + merge(a, b[1:])

n = int(input())
p = list(map(int, input().split()))
found = False

for i in range(2 ** n):
    a = []
    b = []
    for j in range(n):
        if (i & (1 << j)) == 0:
            a.append(p[j])
        else:
            b.append(p[j])
    if len(a) + len(b) == 2 * n and merge(a, b) == p:
        print("YES")
        found = True
        break

if not found:
    print("NO")
