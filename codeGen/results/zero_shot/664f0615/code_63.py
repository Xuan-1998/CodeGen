import sys

t = list(map(int, sys.stdin.readline().split()))
v0, vf = t[0], t[1]
t, dv = map(int, sys.stdin.readline().split())

dv = min(dv, abs(vf - v0))

v = (vf + v0) / 2
d = (vf + v0) * t / 2
print(int(d))
