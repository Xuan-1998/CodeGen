v1, v2 = map(int, input().split())
t, dv = map(int, input().split())

length = (v2 - v1) * t // dv + min(v1, v2)
print(length)
