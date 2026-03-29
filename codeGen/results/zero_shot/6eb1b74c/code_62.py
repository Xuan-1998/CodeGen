import sys

m = 0
used_strings = set()

t = input().strip()
n = int(input())

for i in range(n):
    s = input().strip()
    for j in range(len(t) - len(s) + 1):
        if t[j:j+len(s)] == s:
            used_strings.add(i)
            m += 1

if len(used_strings) == 0:
    print(-1)
else:
    for i in range(m):
        w = min([k for k in used_strings if k > 0])
        used_strings.remove(w)
        print(f"{w} {i}")
