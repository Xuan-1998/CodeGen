def merge(a, b):
    result = []
    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    return result + a + b

n = int(input())
p = list(map(int, input().split()))

a = []
b = []

for x in p:
    if len(a) < n and x not in a:
        a.append(x)
    elif len(b) < n and x not in b:
        b.append(x)

if merge(a, b) == p:
    print("YES")
else:
    print("NO")
