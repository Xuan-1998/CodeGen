from sys import stdin, stdout
n = int(stdin.readline())
p = list(map(int, stdin.readline().split()))
a = set()
b = set()
for i in range(0, n):
    if p[i] < p[n+i]:
        a.add(p[i])
    elif p[i] > p[n+i]:
        b.add(p[n+i])
    else:
        a.add(p[i])

if len(a) + len(b) == 2*n and not a & b:
    stdout.write("YES\n")
else:
    stdout.write("NO\n")
