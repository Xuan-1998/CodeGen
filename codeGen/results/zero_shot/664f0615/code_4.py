v1, v2 = map(int, input().split())
t, dv = map(int, input().split())

max_length = (v2 - v1) / dv * t
print(int(max_length))
