v0, vf = map(int, input().split())
t, dv = map(int, input().split())

print(t * min(vf - v0, 2*dv) + (vf if t % 2 == 1 else v0))
