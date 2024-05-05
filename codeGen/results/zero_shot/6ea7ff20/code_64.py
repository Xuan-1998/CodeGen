def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

p = list(map(int, input().split()))
n = int(input())
p.sort()

for i in range(n):
    for j in range(i + 1, n):
        a = p[:i]
        b = p[i:j]
        if len(set(a).union(set(b))) == n:
            print("YES")
            exit()
print("NO")
