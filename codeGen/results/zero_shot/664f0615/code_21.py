v1, v2 = map(int, input().split())
t, delta_v = map(int, input().split())

print(min(v1 + t * delta_v, v2 - t * delta_v))
