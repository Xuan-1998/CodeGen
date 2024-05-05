code
n = int(input())
p = list(map(int, input().split()))
a = []
b = []

for i in range(len(p)):
    if not a or p[i] < a[-1]:
        a.append(p[i])
    elif not b or p[i] > b[-1]:
        b.append(p[i])

if len(a) + len(b) == 2 * n:
    print("YES")
else:
    print("NO")
