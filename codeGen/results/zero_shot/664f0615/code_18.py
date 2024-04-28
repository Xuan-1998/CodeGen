v0, v1 = map(int, input().split())
t, dv = map(int, input().split())

if dv > 10:
    print(0)
else:
    length = t * (v0 + v1) / 2
    print(int(length))
