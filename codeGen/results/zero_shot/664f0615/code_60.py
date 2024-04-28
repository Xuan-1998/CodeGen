v0, vf = map(int, input().split())
t, dv = map(int, input().split())

print(min(vf - v0, dv) * t)
