import sys
v1, v2 = map(int, input().split())
t, dv = map(int, input().split())

v_avg = (v1 + v2) / 2
print(v_avg * t)
