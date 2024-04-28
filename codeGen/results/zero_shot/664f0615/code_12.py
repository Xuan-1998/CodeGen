v0, vf = map(int, input().split())
t, delta_v = map(int, input().split())

min_speed = min(v0, vf)
max_length = (vf - v0) * t // delta_v + min(t, (vf - v0) * delta_v // (2 * delta_v))

print(max_length)
