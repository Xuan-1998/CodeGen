v0, v1 = map(int, input().split())
t, dv = map(int, input().split())

print((v1 - v0) // dv * (dv + 1) + min(v0, v1))
