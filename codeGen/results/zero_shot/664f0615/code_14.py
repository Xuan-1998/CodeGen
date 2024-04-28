v1, v2 = map(int, input().split())
t, dv = map(int, input().split())

print(min(v2 - v1, t * dv))
