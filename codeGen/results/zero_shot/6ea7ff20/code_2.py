n = int(input())
p = list(map(int, input().split()))
a = set()
b = set()

for i in range(2*n):
    if p[i] % 2 == 0:
        a.add(p[i])
    else:
        b.add(p[i])

if len(a) != n or len(b) != n:
    print("NO")
else:
    print("YES")
