v0, vf = map(int, input().split())
t, dv = map(int, input().split())

print((vf - v0) * (t - 1) // dv + 1)
