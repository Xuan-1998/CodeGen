n = int(input())
p = list(map(int, input().split()))

a = []
b = []

for i in range(n):
    if p[i] < n:
        a.append(p[i])
    else:
        b.append(p[i] - n)

if len(set(a).intersection(b)) == 0:
    print("YES")
else:
    print("NO")
