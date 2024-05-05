import sys
import collections

t = input().strip()
n = int(input())
s = [input().strip() for _ in range(n)]

sa = collections.OrderedDict()

for i in range(len(t)):
    sa[t[i:]] = i

sa = list(sa.keys())

steps = 0

for i in range(len(sa)):
    for s in s:
        if sa[i].startswith(s):
            steps += 1
            break

if steps == -1:
    print(-1)
else:
    print(steps)

for i in range(len(sa)):
        for s in s:
            if sa[i].startswith(s):
                print(i + 1, sa.index(s) + 1)
                break
