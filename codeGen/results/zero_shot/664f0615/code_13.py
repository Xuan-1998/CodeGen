v1, v2 = map(int, input().split())
t, d = map(int, input().split())

max_speed = max(v1, v2)
min_speed = min(v1, v2)

print(min(t * max_speed, (t - 1) * d / (v2 + v1) + (t - 1) * (d % (v2 + v1)) // (v2 - v1)))
