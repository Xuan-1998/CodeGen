n = int(input())
p = list(map(int, input().split()))
a = []
b = []
for x in p:
    if len(a) <= n:
        a.append(x)
    else:
        b.append(x)
if len(set(a) & set(b)) > 0:
    print("NO")
else:
    print("YES")
